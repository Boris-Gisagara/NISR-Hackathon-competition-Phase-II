import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html,callback
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

dash.register_page(__name__, path='/')

#---------------------------------------------------------------------------data importation and charts creation-------------------------------------------------------------------------------------

dataLF = {
    "Status": ["Employed", "Unemployed", "Outside Labor Force"],
    "Not Any": [ 1613706, 362983, 1604550 ],
    "Primary": [ 1153028, 282708, 1183364],
    "L.Secondary": [219337, 68563, 457638],
    "U.Secondary": [315687, 151494, 221957],
    "Univerisity":[244593,51197,32781]
}

df1 = pd.DataFrame(dataLF)
# Creation of a spider chart
fig = go.Figure()

for index, row in df1.iterrows():
    fig.add_trace(go.Scatterpolar(
        r=[row["Not Any"], row["Primary"], row["L.Secondary"], row["U.Secondary"], row["Univerisity"], row['Not Any']],
        theta=["Not Any", "Primary", "L.Secondary", "U.Secondary", "Univerisity", "Not Any"], 
        # fill="toself",
        name=row["Status"]
    ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, df1[["Not Any", "Primary", "L.Secondary", "U.Secondary", "Univerisity"]].max().max()],
            showgrid=True,       # Show the radial grid lines
            gridwidth=1,         # Set the width of the grid lines
            gridcolor='#233336'    # Set the color of the grid lines to black
        )
    )
)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# data frame for migration 
gender_data = {
    'Category': ['Male', 'Female'],
    'Internal Migrants - Employed': [273936, 222971],
    'Internal Migrants - Unemployed': [40828, 66802],
    'Internal Migrants - Outside Labour Force': [69352, 175831],
    'International Migrants - Employed': [13566, 6696],
    'International Migrants - Unemployed': [3214, 2158],
    'International Migrants - Outside Labour Force': [5897, 6655]
}

residence_data = {
    'Category': ['Urban', 'Rural'],
    'Internal Migrants - Employed': [268599, 228308],
    'Internal Migrants - Unemployed': [51195, 56434],
    'Internal Migrants - Outside Labour Force': [97015, 148168],
    'International Migrants - Employed': [9010, 11253],
    'International Migrants - Unemployed': [2508, 2864],
    'International Migrants - Outside Labour Force': [5461, 7091]
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

dataTP = {
    'Age_Range': [
        '0-4', '5-9', '10-14 ', '15-19 ', '20-24 ', '25-29 ',
        '30-34 ', '35-39 ', '40-44 ', '45-49 ', '50-54 ', '55-59 ',
        '60-64 ', '65-69 ', '70-74 ', '75+'
    ],
    'Total': [
        1553553, 1628364, 1600085, 1661630, 1157947, 896904, 860513, 820692,
        707625, 490542, 419950, 343320, 333960, 246318, 164846, 191780
    ],
    'Male': [
        776063, 823677, 804702, 820717, 580976, 413564, 422771, 387942,
        326904, 216429, 184435, 164035, 151138, 105437, 71231, 69883
    ],
    'Female': [
        777490, 804687, 795383, 840913, 576971, 483339, 437742, 432749,
        380721, 274113, 235516, 179285, 182822, 140881, 93616, 121898
    ],
    'Urban': [
        298673, 277015, 241973, 291405, 277902, 227985, 221883, 180065,
        146620, 91497, 68406, 57024, 44635, 34132, 19807, 24061
    ],
    'Rural': [
        1254880, 1351348, 1358113, 1370225, 880045, 668919, 638630, 640626,
        561004, 399045, 351544, 286296, 289325, 212186, 145039, 167719
    ]
}
# Create a DataFrame from the dataTP
df2 = pd.DataFrame(dataTP)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# data for disabilities table
# data_path = r"C:\Users\user\OneDrive\Documents\python works\labor_force\dataset\disability1.xlsx"
# Link to the dataset on GitHub
disability1_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/disability1.xlsx'

# Load the dataset
dfdisability2 = pd.read_excel(disability1_url, engine='openpyxl')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for the pie chart on employment status among disabled persons
# Link to the dataset on GitHub
disability2_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/disability2.xlsx'

# Load the dataset
Disability2 = pd.read_excel(disability2_url, engine='openpyxl')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#load the dataset for migration
# Link to the dataset on GitHub
migrants_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Migrants.xlsx'

# Load the dataset
Migrants = pd.read_excel(migrants_url, engine='openpyxl')

# Link to the dataset on GitHub
internal_migrants_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Internal_migrants.xlsx'

# Load the dataset
Internal_migrants = pd.read_excel(internal_migrants_url, engine='openpyxl')

# Link to the dataset on GitHub
international_migrants_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/International_migrants.xlsx'

# Load the dataset
International_migrants = pd.read_excel(international_migrants_url, engine='openpyxl')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Link to the dataset on GitHub
migrants_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/df_migrants.xlsx'

# Load the dataset
migrants = pd.read_excel(migrants_url, engine='openpyxl')

# Link to the dataset on GitHub
internal_migrants_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/df_internal_migrants.xlsx'

# Load the dataset
internal_migrants = pd.read_excel(internal_migrants_url, engine='openpyxl')
# Link to the dataset on GitHub
international_migrants_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/df_international_migrants.xlsx'

# Load the dataset
international_migrants = pd.read_excel(international_migrants_url, engine='openpyxl')
#---------------------------------------------------------------------------Overview page layout----------------------------------------------------------------------------------------
# Define the content for the Overview page
layout = dbc.Container(
    [
        #------------------------------------------------------------------------------------------------------------------------
        # Horizontal frame for the title for "The Labor Force" section
        html.Br(),
        html.Br(),
        html.H1('Overview',style={'textAlign':'center','fontSize': '30px','color': 'black','fontFamily':'Roboto Slab'},className='m-3'),
        html.Br(),
        html.Div(
            [
                html.H3("Whole Country Population Overview", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
#------------------------------------------------------Cards Section---------------------------------------------------------------------------------------------
        # Four cards for labor force statistics in a grid layout
        dbc.Row([
            # Card 1: Total Population
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.Div("13,078,028", style={'fontSize': '20px', 'color': 'black'}),
                        html.Div("Whole Country Population", style={'fontSize': '16px', 'color': 'black'}),
                    ], className="border-start border-info border-5"),
                ],className="text-center m-4"),
                width=3

            ),
            #----------------------------------------------------------------------------------------------------------------------
            # Card 2: Working Age Population
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.Div("7,963,586", style={'fontSize': '20px','color': 'black'}),
                        html.Div("Working Age Population (16+)", style={'fontSize': '16px','color': 'black'}),
                    ],className="border-start border-info border-5")
                ],className="text-center m-4"),
                width=3
            ),
            #----------------------------------------------------------------------------------------------------------------------
            # Card 3: Labor Force
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.Div("4,463,296 ", style={'fontSize': '20px','color': 'black'}),
                        html.Div("Labor Force Population", style={'fontSize': '16px','color': 'black'}),
                    ],className="border-start border-info border-5")
                ],className="text-center m-4"),
                width=3
            ),
            #-----------------------------------------------------------------------------------------------------------------------
            # Card 4: Outside Labor Force Population
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.Div("3,500,290 ", style={'fontSize': '20px','color': 'black'}),
                        html.Div("Outside Labor Force Population", style={'fontSize': '16px','color': 'black'}),
                    ],className="border-start border-info border-5")
                ],className="text-center m-4"),
                width=3
            ),
        ], className="mt-4"),
        html.Br(),
#----------------------------------------------------------------------------------------Graphs Section-------------------------------------------------------------------------------------------     
        dbc.Row([
            # Graph 1: Total Population by Age Group
            dbc.Col(
                html.Div([
                    html.Div([
                        html.H3("Total Population by Age Group", style={'color': 'black','textAlign':'center', 'margin': '0 auto'}),
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    dcc.Graph(
                    figure=px.bar(df2, x='Age_Range', y='Total',
                    ),
                    style={'height': '400px'}
                ),                    
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
                
                width=4
            ),
            #-----------------------------------------------------------------------------------------------------------------------
            # Graph 2: Total Population by Gender
            dbc.Col(
                html.Div([
                    html.Div([
                        html.H3("Total Population by Gender", style={'color': 'black','textAlign':'center', 'margin': '0 auto'}),
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    dcc.Graph(
                    figure=px.bar(df2, x='Age_Range', y=['Male', 'Female'],
                                #    title="Total Population by Gender"
                                   ),
                    style={'height': '400px'}
                ),
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
                
                width=4
            ),
            #------------------------------------------------------------------------------------------------------------------------
            # Graph 3: Total Population by Residence Area
            dbc.Col(
                html.Div([
                    html.Div([
                        html.H3("Total Population by Residence Area", style={'color': 'black','textAlign':'center', 'margin': '0 auto'}),
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    dcc.Graph(
                    figure=px.bar(df2, x='Age_Range', y=['Urban', 'Rural'],
                                #    title="Total Population by Residence Area"
                                   ),
                    style={'height': '400px'}
                ),
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
                
                width=4
            ),
        ], className="mt-4"),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        html.Br(),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Working Age Population Demographics", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3("Employment Status Among Population(16+) by Education Attained", style={'color': 'black','textAlign':'center', 'margin': '0 auto'}),
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                                       
                    dcc.Graph(figure=fig),
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
                
                ],width=6
            ),
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3("Employment Status Among Population(16+) by Gender/Residence", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'}),
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Select Status:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dcc.Dropdown(
                                id='dropdown-input',
                                options=[
                                    {'label': 'Employed', 'value': 'Employed'},
                                    {'label': 'Unemployed', 'value': 'Unemployed'},
                                    {'label': 'Outside The Labor', 'value': 'Outside The Labor'}
                                ],
                                value='Employed',  # Default selection
                                style={
                                    'width': '100%',
                                    'textAlign': 'center',
                                    'fontSize': '15px',  # Adjust font size
                                    'borderRadius': '8px',  # Add rounded corners 
                                },
                                clearable=False,
                                searchable=False,
                                className='m-2'
                            ),
                        ],width=6),
                        dbc.Col([
                            html.Div([
                                html.H3("Select Category:",style={'fontSize':'16px'})
                            ],className='m-2',style={'textAlign': 'center'}),
                                dbc.Form([
                                    html.Div([
                                        dbc.RadioItems(
                                            id='radio-input',
                                            options=[
                                                {'label': 'Gender', 'value': 'gender'},
                                                {'label': 'Residence', 'value': 'Residence'}
                                            ],
                                            value='gender',  # Default selection
                                            inline=True,
                                            labelStyle={'display': 'block'},
                                            className='custom-radio m-2',
                                            style={'textAlign': 'center'}
                                        ),
                                    ]),
                                ]),
                        ],width=6)
                    ]),                
                    html.Br(),
                    dcc.Graph(id='bar-chart'),
                ], style={'border': '2px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),       
            ], width=6            
        ),
    ]),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        html.Br(),
        dbc.Row([
            # Horizontal frame for the title for "Disabled Persons" section
            html.Div(
                [
                    html.H3("Disabled Persons by Gender/Residence/Age Group", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
                ],
                style={'textAlign': 'center'}
            ),
            dbc.Col([
                html.Div([
                    html.Div([
                    html.H3("Disabled persons by Type of Disability/Gender/Residence/Age group", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    dbc.Row([
                        dbc.Col([
                                dbc.Form([
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                html.H3("Choose category:", style={'fontSize':'16px'})
                                            ], className='m-2', style={'textAlign': 'center'}),
                                            dbc.RadioItems(
                                                id='radio-pyramid',
                                                options=[
                                                    {'label': 'Age group', 'value': 'Age group'},
                                                    {'label': 'Residence', 'value': 'residence'}
                                                ],
                                                value='Age group',
                                                labelStyle={'display': 'inline-block', 'margin-right': '10px'},
                                                inline=True,
                                                className='custom-radio m-2',
                                                style={'textAlign': 'center'}
                                            ),
                                        ]),
                                        dcc.Graph(id='pyramid-disabled')
                                    ]),
                                ]),
                                
                            ]),
                    ])
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),            
                ],width=7
            ),
            # Updated layout with a dropdown 
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3("Labor Force Status among Disabled persons", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                        ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                    #-------------------------------------------------------------------------------------------------------------------------------------------
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Select Status:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dcc.Dropdown(
                                id='employment-dropdown',
                                options=[
                                    {'label': 'Employed', 'value': 'Employed'},
                                    {'label': 'Unemployed', 'value': 'Unemployed'},
                                    {'label': 'Outside labor force', 'value': 'Outside labour force'}
                                ],
                                value='Employed',  # Default selected option
                                style={'width': '70%','textAlign': 'center'},
                                clearable=False,
                                searchable=False,
                                className='m-2'
                            ),
                        ],width=12)
                    ]),
                    html.Br(),
                    dcc.Graph(id='pie-chart'),
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
            ], width=5)
        ]),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        html.Br(),
        # Horizontal frame for the title for "Disabled Persons" section
            html.Div(
                [
                    html.H3("Employment Status among Internal and International Immigrants", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
                ],
                style={'textAlign': 'center'}
            ),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3("Migrant Population by the Reason of Moving and Labor Force Status", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                        ],className="border-start border-primary border-5 m-4", style={'height': '40px'}
                    ),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Select Type of Migration:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dcc.Dropdown(
                                id='Mig-dropdown',
                                options=[
                                    {'label': 'Migrants', 'value': 'Migrants'},
                                    {'label': 'Internal migrants', 'value': 'Internal migrants'},
                                    {'label': 'International migrants', 'value': 'International migrants'}
                                ],
                                value='Migrants',
                                style={
                                    'width': '70%',
                                    'textAlign': 'center',                      
                                    },
                                    clearable=False,
                                    searchable=False,
                                    className='m-2'
                            ),
                        ],width=12)
                    ]),
                    html.Br(),
                    dcc.Graph(id='Mig-barChart'),
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'})
            ],width=6),
            dbc.Col([
                html.Div([
                    html.Div([
                    html.H3("Immigrant Labor Force Status by Gender and Residence Area", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}
                    ),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Select Type of Migration:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            # Dropdown to select dataset
                            dcc.Dropdown(
                                id='migrada',
                                options=[
                                    {'label': 'Internal Migrants', 'value': 'Internal Migrants'},
                                    {'label': 'International Migrants', 'value': 'International Migrants'}
                                ],
                                value='Internal Migrants',   # Default selected dataset
                                style={
                                    'width': '100%',
                                    'textAlign': 'center',
                                    },
                                clearable=False,
                                searchable=False,
                                className='m-2'
                            ),

                        ],width=6),
                        dbc.Col([
                            html.Div([
                                html.H3("Choose Type of Migration:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dbc.RadioItems(
                                id='migrarad',
                                options=[
                                    {'label': 'Gender', 'value': 'Gender'},
                                    {'label': 'Residence', 'value': 'Residence'}
                                ],
                                value='Gender',  # Default value, change as needed
                                labelStyle={'display': 'inline-block', 'marginRight': '10px'},
                                inline=True,
                                className='custom-radio m-2',
                                style={'textAlign': 'center'},                                
                            ),
                        ],width=6)
                    ]),
                    
                    # Graph to display the horizontal grouped bar chart
                    dcc.Graph(id='migrabar')
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'})
            ],width=6)
        ]),
        html.Br(),   
    ],
    
    fluid=True
),
#-------------------------------------------------------------------------------------Callback section----------------------------------------------------------------------------------------------
# Callback to update the pie chart based on the slider value
# Updated callback using the dropdown value
@callback(
    Output('pie-chart', 'figure'),
    [Input('employment-dropdown', 'value')]
)
def update_pie_chart(selected_value):
    selected_data = Disability2[['Type of disability', selected_value]].copy()

    # Convert values to numeric
    selected_data.loc[:, selected_value] = pd.to_numeric(
        selected_data[selected_value], errors='coerce'
    )

    # Create pie chart
    figPie = px.pie(
        selected_data,
        names='Type of disability',
        values=selected_value,
        title=f'Disabled persons Who are {selected_value}'
    )

    # Update layout for better visualization
    figPie.update_layout(
        title=dict(
            text=f'Disabled persons Who are {selected_value}',
            x=0.5,  # Centered title
            y=0.95,  # Positioned at the top
            xanchor='center',
            yanchor='top',
            font=dict(size=16, color='black')  # Adjust font size as needed
        )
    )

    return figPie

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update the bar chart based on the selected dataset for migration
@callback(
    Output('Mig-barChart', 'figure'),
    [Input('Mig-dropdown', 'value')]
)
def update_graph(selected_dataset):
    if selected_dataset == 'Migrants':
        migri = Migrants
    elif selected_dataset == 'Internal migrants':
        migri = Internal_migrants
    elif selected_dataset == 'International migrants':
        migri = International_migrants

    figure = {
        'data': [
            {'y': migri['Reasons'], 'x': migri['Employed'], 'type': 'bar', 'name': 'Employed', 'orientation': 'h'},
            {'y': migri['Reasons'], 'x': migri['Unemployed'], 'type': 'bar', 'name': 'Unemployed', 'orientation': 'h'},
            {'y': migri['Reasons'], 'x': migri['Outside Labour Force'], 'type': 'bar', 'name': 'Outside Labour Force', 'orientation': 'h'}
        ],
        'layout': {
            'title': f'{selected_dataset} Distribution with the Reasons',
            'barmode': 'group',
            'hovermode': 'closest',
            'yaxis': {'title': '', 'tickfont': {'size': 6}, 'fontcolor': 'black','textAlign':'auto'},
            'xaxis': {'title': 'Population'},
            'hoverlabel': {'bgcolor': 'white'},
            'legend': {'x': 1, 'y': 1.0}
        }
    }

    return figure
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@callback(
    Output('bar-chart', 'figure'),
    [Input('radio-input', 'value'),
     Input('dropdown-input', 'value')]
)
def update_bar_chart(selected_radio, selected_dropdown):
    df3=pd.read_excel(r'C:\Users\user\OneDrive\Documents\python works\labor_force\dataset\labor.xlsx')
    if selected_radio == 'gender':
        # Filter the data for the selected gender (male/female)
        filtered_data = df3[df3['Status'] == selected_dropdown][['Age Groups', 'Male Pop', 'Female Pop']]
        x = 'Age Groups'
        y1 = 'Male Pop'
        y2 = 'Female Pop'
        title = f"{selected_dropdown} Population by Age Group and Gender"
        hover_text = ['Male', 'Female']
        legend_labels = {'Male': 'Male', 'Female': 'Female'}
    else:
        # Filter the data for the selected residence (urban/rural)
        filtered_data = df3[df3['Status'] == selected_dropdown][['Age Groups', 'Urban Pop', 'Rural Pop']]
        x = 'Age Groups'
        y1 = 'Urban Pop'
        y2 = 'Rural Pop'
        title = f"{selected_dropdown} Population by Age Group and Residence"
        hover_text = ['Urban', 'Rural']
        legend_labels = {'Urban': 'Urban', 'Rural': 'Rural'}

    # Create the bar chart using plotly.graph_objects
    figureBar = go.Figure()

    figureBar.add_trace(go.Bar(
        x=filtered_data[x],
        y=filtered_data[y1],
        name=legend_labels[hover_text[0]],
        hovertext=hover_text[0],
        marker_color='rgb(26, 118, 255)'  # Adjust color as needed
    ))

    figureBar.add_trace(go.Bar(
        x=filtered_data[x],
        y=filtered_data[y2],
        name=legend_labels[hover_text[1]],
        hovertext=hover_text[1],
        marker_color='rgb(55, 83, 109)'  # Adjust color as needed
    ))

    figureBar.update_layout(
        title=dict(
            text=title,
            x=0.5,  # Centered title
            y=0.95,  # Positioned at the top
            xanchor='center',
            yanchor='top',
            font=dict(size=16, color='black')  # Adjust font size as needed
        ),
        xaxis=dict(title='Age Groups'),
        yaxis=dict(title='Population'),
        barmode='group'
    )

    return figureBar
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Define callback to update bar chart based on user input
@callback(
    Output('migrabar', 'figure'),
    [
        Input('migrada', 'value'),
        Input('migrarad', 'value')
    ]
)
def update_bar_chart(selected_dataset, selected_group):
    if selected_dataset == 'Internal Migrants':
        data = gender_data if selected_group == 'Gender' else residence_data
    elif selected_dataset == 'International Migrants':
        data = gender_data if selected_group == 'Gender' else residence_data
    else:
        return {}

    figMigration2 = px.bar(
        data,
        x='Category',
        y=[
            f'{dataset} - {status}' for dataset in [selected_dataset] for status in
            ['Employed', 'Unemployed', 'Outside Labour Force']
        ],
        barmode='group',
        labels={'value': 'Population', 'variable': ''},
        title=f'{selected_dataset}  by {selected_group}',
        color_discrete_sequence=['lightblue', 'darkblue', 'lightgreen'],
        category_orders={'variable': ['Employed', 'Unemployed', 'Outside Labour Force']}
    )
    fig.update_layout(
        legend=dict(
            orientation='h',
            xanchor='center',
            yanchor='bottom'
        )
    )
    return figMigration2

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@callback(
    Output('pyramid-disabled', 'figure'),
    [Input('radio-pyramid', 'value')]
)
def update_pyramid_chart(selected_option):
    if selected_option == 'Age group':
        labels = ['Seeing', 'Hearing', 'Walking', 'Remembering', 'Washing, dressing', 'Communicating']
        male_data = dfdisability2['5-15 yrs'].tolist()
        female_data = [-1 * value for value in dfdisability2['16+ yrs'].tolist()]  # Negative values for females
        title = 'Time related underemployment by disability/Age group'
    else:
        labels = ['Seeing', 'Hearing', 'Walking', 'Remembering', 'Washing, dressing', 'Communicating']
        urban_data = dfdisability2['Urban'].tolist()
        rural_data = [-1 * value for value in dfdisability2['Rural'].tolist()]  # Negative values for rural
        title = 'Time related underemployment by disability/Residence area'

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=labels,
        x=male_data if selected_option == 'Age group' else urban_data,
        orientation='h',
        name='5-15 yrs' if selected_option == 'Age group' else 'Urban',
        marker=dict(color='#e8422c')
    ))
    fig.add_trace(go.Bar(
        y=labels,
        x=female_data if selected_option == 'Age group' else rural_data,
        orientation='h',
        name='16+ yrs' if selected_option == 'Age group' else 'Rural',
        marker=dict(color='#e8b92c')
    ))
    # Update layout for better visualization
    fig.update_layout(
        barmode='relative',
        title=dict(
            text=title,
            x=0.5,  # Centered title
            y=0.95,  # Positioned at the top
            xanchor='center',
            yanchor='top',
            font=dict(size=16, color='black')  # Adjust font size as needed
        )
    )
    return fig
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------