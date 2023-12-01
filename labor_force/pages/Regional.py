import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html,Input, Output,callback
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go
import geopandas as gpd

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

dash.register_page(__name__, path='/Regional')

#----------------------------------------------------------------------------------------Data and charts creation-------------------------------------------------------------------------------------------

# Data
dataDis = {
    'Districts': ['Nyarugenge', 'Gasabo', 'Kicukiro', 'Nyanza', 'Gisagara', 'Nyaruguru', 'Huye', 'Nyamagabe', 'Ruhango', 'Muhanga', 'Kamonyi', 'Karongi', 'Rutsiro', 'Rubavu', 'Nyabihu', 'Ngororero', 'Rusizi', 'Nyamasheke', 'Rulindo', 'Gakenke', 'Musanze', 'Burera', 'Gicumbi', 'Rwamagana', 'Nyagatare', 'Gatsibo', 'Kayonza', 'Kirehe', 'Ngoma', 'Bugesera'],
    'Employed': [ 155687, 292464, 199478, 90187, 93130, 84801, 112779, 107077, 113408, 108598, 101499, 102608, 92073, 119900, 94554, 82937, 96035, 61936, 92054, 120170, 156766, 94997, 135900, 123759, 136485, 145820, 131666, 102948, 104590, 92044 ],
    'Unemployed': [ 40232, 78762, 52090, 24406, 24542, 23747, 27643, 30001, 29311, 34385, 28817, 30047, 22933, 29533, 22289, 17682, 26898, 21556, 27777, 24370, 36034, 30532, 35455, 30188, 32707, 42392, 24914, 19706, 19372, 28625],
    'Outside Labour Force': [99870, 184387, 113810, 117332, 100154, 139515, 102916, 124909, 135662, 114940, 121055, 126220, 92949, 96000, 83176, 77374, 121156, 100527, 99477, 134503, 125298, 86504, 141072, 131172, 148586, 125323, 159255, 109528, 85737, 101882],
    'Labour Force Participation Rate': [66.2, 66.8, 68.9, 49.4, 54, 43.8, 57.7, 52.3, 51.3, 55.4, 51.8, 51.2, 55.3, 60.9, 58.4, 56.5, 50.4, 45.4, 54.6, 51.8, 60.6, 59.2, 54.8, 54.6, 54, 53.2, 49.6, 52.8, 59.1, 54.2],
    'Unemployment rate': [20.5, 21.2, 20.7, 21.3, 20.9, 1.9, 19.7, 21.9, 20.5, 24, 22.1, 22.7, 19.9, 19.8, 19.1, 17.6, 21.9, 25.8, 23.2, 16.9, 18.7, 24.3, 20.7, 19.6, 19.3, 22.5, 15.9, 16.1, 15.6, 23.7],
    'Employment to population ratio': [52.6, 52.6, 54.6, 38.9, 42.8, 34.2, 46.3, 40.9, 40.7, 42.1, 40.4, 39.6, 44.3, 48.9, 47.3, 46.6, 39.3, 33.7, 42, 43.1, 49.3, 44.8, 43.5, 43.4, 42.9, 46.5, 41.7, 44.3, 49.9, 41.4]
}

# Create a DataFrame
dfDis = pd.DataFrame(dataDis)
dfDis.to_excel('district.xlsx', index = False)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load the shapefile
# Link to the shapefile folder on GitHub
rw_shapefile_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/RwShapeFile'

# Use the link directly to access the shapefiles as needed in your code
shapefile_path = rw_shapefile_url + '/Rwanda.shp'
gdf = gpd.read_file(shapefile_path)
gdf.rename(columns={'ADM2_EN': 'Districts'}, inplace=True)

# Load the employment data
# Link to the dataset on GitHub
districts_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Districts.xlsx'

# Load the dataset
employment_df = pd.read_excel(districts_url, engine='openpyxl')

# Merge the dataframes on the 'Districts' column
merged_df = pd.merge(gdf, employment_df, on='Districts', how='left')
#--------------------------------------------------------------------------------------Regional summary page layout---------------------------------------------------------------------------------------------
layout = dbc.Container([
        html.Br(),
        html.Br(),
        html.H1('Regional Summary',style={'textAlign':'center','fontSize': '30px','color': 'black','fontFamily':'Roboto Slab'},className='m-3'),
        html.Br(),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Labour Force Participation Rate and Unemployment Rate by Districts", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3("Select District:",style={'fontSize':'16px'})
                    ],className='m-2'),
                # Modify the dropdown component in the layout to set the initial value as a list of all provinces
                dcc.Dropdown(
                    id='Districts-dropdown',
                    options=[{'label': Districts, 'value': Districts} for Districts in dfDis['Districts']],
                    value=dfDis['Districts'][0],  # Set the initial value as a list containing the first province or any default province
                    style={
                        'width': '50%',
                        'textAlign': 'center',
                        'fontSize': '15px',  # Adjust font size
                        'borderRadius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False,
                    className='m-2'
                    )                
            ])                
            ],width=12
            ),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.Div([dcc.Graph(id='participation-gauge'),
                ],style={'border': '2px solid #ccc'}),
                
            ],width=4
            ),
            dbc.Col([
                html.Div([dcc.Graph(id='unemployment-gauge'),
                ],style={'border': '2px solid #ccc'}),
                                 
            ],width=4
            ),
            dbc.Col([
                html.Div([dcc.Graph(id='employment-gauge'),
                ],style={'border': '2px solid #ccc'}),
            ],width=4
            )
        ]),
        html.Br(),
        html.Div(
                [
                    html.H3("Labor and Outside Labor Force Poputation by districts", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
                ],
                style={'textAlign': 'center'}
            ),
        html.Div([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H3("Select Status:",style={'fontSize':'16px'})
                ],className='m-2'),
                # Dropdown for selecting the variable to display on the map
                dcc.Dropdown(
                    id='variable-dropdown',
                    options=[
                        {'label': 'Employed', 'value': 'Employed'},
                        {'label': 'Unemployed', 'value': 'Unemployed'},
                        {'label': 'Outside Labour Force', 'value': 'Outside_labour_force'}
                    ],
                    value='Employed',
                    style={
                        'width': '50%',
                        'textAlign': 'center',
                        'fontSize': '15px',  # Adjust font size
                        'borderRadius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False,
                    className='m-2'
                ),
            ]),
        ]),
        # Map
        dcc.Graph(id='map'),
        ], style={'border': '2px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
        html.Br(),
    ],
fluid=True
)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Define callback to update the gauge charts based on the selected province
@callback(
    [Output('participation-gauge', 'figure'),
     Output('unemployment-gauge', 'figure'),
     Output('employment-gauge', 'figure')],
    [Input('Districts-dropdown', 'value')]
)
def update_gauge_charts(selected_Districts):
    participation_rate = dfDis.loc[dfDis['Districts'] == selected_Districts, 'Labour Force Participation Rate'].values[0]
    unemployment_rate = dfDis.loc[dfDis['Districts'] == selected_Districts, 'Unemployment rate'].values[0]
    employment_rate= dfDis.loc[dfDis['Districts'] == selected_Districts, 'Employment to population ratio'].values[0]
    
    participation_fig = go.Figure(go.Indicator(
        mode='gauge+number',
        value=participation_rate,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "darkblue"},
               'steps': [
                   {'range': [0, 50], 'color': "lightgray"},
                   {'range': [50, 100], 'color': "lightgray"}
                   ],

               }
    ))
    participation_fig.update_layout(
        title_text=f"Labour Force Participation Rate - {selected_Districts}",title_x=0.5)
    
    unemployment_fig = go.Figure(go.Indicator(
        mode='gauge+number',
        value=unemployment_rate,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "darkblue"},
               'steps': [
                   {'range': [0, 50], 'color': "lightgray"},
                   {'range': [50, 100], 'color': "lightgray"}],

               }
    ))
    unemployment_fig.update_layout(
        title_text=f"Unemployment Rate - {selected_Districts}",title_x=0.5)
    
    employment_fig = go.Figure(go.Indicator(
        mode='gauge+number',
        value=employment_rate,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "darkblue"},
               'steps': [
                   {'range': [0, 50], 'color': "lightgray"},
                   {'range': [50, 100], 'color': "lightgray"}
                   ],

               }
    ))
    employment_fig.update_layout(
        title_text=f"Employment to population ratio- {selected_Districts}",title_x=0.5)
    
    return participation_fig, unemployment_fig, employment_fig
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update the map based on the selected variable
@callback(
    Output('map', 'figure'),
    [Input('variable-dropdown', 'value')]
)
def update_map(selected_variable):
    fig = px.choropleth_mapbox(
        merged_df,
        geojson=gdf.geometry,
        locations=merged_df.index,
        color=selected_variable,
        color_continuous_scale="Viridis",
        hover_name='Districts',
        mapbox_style="carto-positron",
        center={"lat": -1.9403, "lon": 29.8739},  # Set to a location within Rwanda
        # zoom=8,  # Adjust the zoom level as needed
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
