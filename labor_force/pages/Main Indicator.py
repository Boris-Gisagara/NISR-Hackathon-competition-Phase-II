import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html,callback,Input,Output
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

dash.register_page(__name__, path='/Main_Indicators')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Link to the dataset on GitHub
dfrate_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/indicator-Age.xlsx'

# Load the dataset
dfrate = pd.read_excel(dfrate_url, engine='openpyxl')

# Link to the dataset on GitHub
edu_indicator_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/edu_levelrate.xlsx'

# Load the dataset
EduIndicator = pd.read_excel(edu_indicator_url, engine='openpyxl')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Link to the dataset on GitHub
econoagri_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Econoagri.xlsx'

# Load the dataset
Econoagri = pd.read_excel(econoagri_url, engine='openpyxl')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load the dataset for employed population IN/NOT in agriculture
# Link to the dataset on GitHub
employ_agri_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/EmployAgri.xlsx'

# Load the dataset
employ_agri = pd.read_excel(employ_agri_url, engine='openpyxl')
# Filter data for those in agriculture and not in agriculture
in_agriculture = employ_agri[employ_agri['Type'] == 'In Agriculture']
not_in_agriculture = employ_agri[employ_agri['Type'] == 'Not in Agriculture']

# Create a radar chart for those in agriculture
figEmplAgr = go.Figure()

figEmplAgr.add_trace(go.Scatterpolar(
    r=in_agriculture['Population'],
    theta=in_agriculture['CategoryAgri'],
    # fill='toself',
    name='In Agriculture'
))

# Create a radar chart for those not in agriculture
figEmplAgr.add_trace(go.Scatterpolar(
    r=not_in_agriculture['Population'],
    theta=not_in_agriculture['CategoryAgri'],
    # fill='toself',
    name='Not in Agriculture'
))

# Update layout for better visualization
figEmplAgr.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, max(employ_agri['Population'])])
    ),
    showlegend=True,
)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Link to the dataset on GitHub
age_pop_agri_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/agerangeagri.xlsx'

# Load the dataset
AgePopAgri = pd.read_excel(age_pop_agri_url, engine='openpyxl')
#---------------------------------------------------------------------------Agriculture page layout-----------------------------------------------------------------------------------
layout = dbc.Container([
        html.Br(),
        html.Br(),
        html.H1('Main Indicators',style={'textAlign':'center','fontSize': '30px','color': 'black','fontFamily':'Roboto Slab'},className='m-3'),
        html.Br(),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Trend of  Main indicators across Population age range", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
        dbc.Row([
            html.Div([
                html.Div([
                    html.H3("Select Indicator:",style={'fontSize':'16px'})
                ],className='m-2'),
                dcc.Dropdown(
                    id='dropdownrat-select',
                    options=[
                        {'label': 'Labour Force Participation Rate', 'value': 'Labour force participation rate'},
                        {'label': 'Employment to Population Ratio', 'value': 'Employment-population ratio'},
                        {'label': 'Unemployment Rate', 'value': 'Unemployment rate'}
                    ],
                    value='Labour force participation rate',  # Default selected value
                    style={
                        'width': '60%',
                        'textAlign': 'center',
                        'fontSize': '15px',
                        'borderRadius': '8px',
                    },
                    clearable=False,
                    searchable=False,
                    className='m-2'
                ),

                dcc.Graph(
                    id='line-chart'
                )
            ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
        ]),
        html.Br(),
        html.Div(
            [
                html.H3("Main Indicators in Education", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
        dbc.Row([
            html.Div([
                html.Div([
                    html.H3("Select Education Level:",style={'fontSize':'16px'})
                ],className='m-2'),
                dcc.Dropdown(
                    id='dropdown-edu-level',
                    options=[{'label': level, 'value': level} for level in EduIndicator['Educational_level']],
                    value='Not any',
                    style={
                            'width': '70%',
                            'textAlign': 'center',
                            'fontSize': '15px',  # Adjust font size
                            'borderRadius': '8px',  # Add rounded corners 
                            },
                        clearable=False,
                        searchable=False,
                        className='m-2'
                ),
                html.Div([dcc.Graph(id='guagelaf')], style={'width': '33%', 'display': 'inline-block'}),
                html.Div([dcc.Graph(id='gaugeempratio')], style={'width': '33%', 'display': 'inline-block'}),
                html.Div([dcc.Graph(id='gaugeunemplor')], style={'width': '33%', 'display': 'inline-block'}),
            ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'})            
        ]),
#-------------------------------------------------------------------existing------------------------------------------------------------------------------------
        html.Br(),
    ],
    fluid=True
)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@callback(
    Output('line-chart', 'figure'),
    [Input('dropdownrat-select', 'value')]
)
def update_line_chart(selected_value_rat):
    trace = {
        'x': dfrate['Age_grouprate'],
        'y': dfrate[selected_value_rat],
        'type': 'line',
        'name': selected_value_rat
    }

    fig = {
        'data': [trace],
        'layout': {
            'title': f'Trend of {selected_value_rat} Over Population 16+ age range',
            'xaxis': {'title': 'Age Group'},
            'yaxis': {
                'title': f'{selected_value_rat}',
                'range': [0, 100],  # Set a fixed range for the y-axis
                'dtick': 10,  # Adjust the interval for y-axis tick marks
                'grid': {'show': True, 'color': '#00ff00', 'dash': 'dash'},  # Add grid lines
            },
            'hovermode': 'closest'
        }
    }

    return fig
#---------------------------------------------------------------------------------------------------------------------------------------
@callback(
    [Output('guagelaf', 'figure'),
     Output('gaugeempratio', 'figure'),
     Output('gaugeunemplor', 'figure')],
    [Input('dropdown-edu-level', 'value')]
)
def update_gauge_charts(selected_edu_level):
    selected_row = EduIndicator[EduIndicator['Educational_level'] == selected_edu_level]

    figures = []

    for i, col in enumerate(['Labour force participation rate', 'Employment-to population ratio', 'Unemployment rate']):
        value = selected_row[col].values[0]

        figure = go.Figure(go.Indicator(
            mode='gauge+number',
            value=value,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': f'{col}<br>{selected_edu_level}'},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': 'darkblue'},
                   'steps': [
                       {'range': [0, 100], 'color': 'lightgray'},
                       
                   ]}))

        figures.append(figure)

    return figures