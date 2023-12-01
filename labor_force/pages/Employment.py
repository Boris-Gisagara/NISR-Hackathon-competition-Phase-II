import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html,callback
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go
from math import pi
import matplotlib.pyplot as plt
from dash.dependencies import Input, Output
from mpldatacursor import datacursor
import textwrap
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

dash.register_page(__name__, path='/Employment')

#------------------------------------------------------------------------------Data and charts creation-------------------------------------------------------------------
#data for formal and informal sector 
# Link to the dataset on GitHub
formal_sector_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/formal_sector.xlsx'

# Load the dataset
formal_sector = pd.read_excel(formal_sector_url, engine='openpyxl')

# Link to the dataset on GitHub
informal_sector_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/informal_sector.xlsx'

# Load the dataset
informal_sector = pd.read_excel(informal_sector_url, engine='openpyxl')

# Link to the dataset on GitHub
formal_sector_out_of_agri_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/formal_sector_out_of_agri.xlsx'

# Load the dataset
formal_sector_out_of_agri = pd.read_excel(formal_sector_out_of_agri_url, engine='openpyxl')

# Link to the dataset on GitHub
informal_sector_out_of_agri_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/informal_sector_out_of_agri.xlsx'

# Load the dataset
informal_sector_out_of_agri = pd.read_excel(informal_sector_out_of_agri_url, engine='openpyxl')


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for the employment status in rwanda for the heatmap
# Load the data
# Link to the dataset on GitHub
economic_activity_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Economic.xlsx'

# Load the dataset
economic_activity_df = pd.read_excel(economic_activity_url, engine='openpyxl')
# Link to the dataset on GitHub
age_range_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Age_range.xlsx'

# Load the dataset
age_range_df = pd.read_excel(age_range_url, engine='openpyxl')
# Link to the dataset on GitHub
occupations_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Occupations.xlsx'

# Load the dataset
occupation_df = pd.read_excel(occupations_url, engine='openpyxl')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for job creation and working time
# Link to the dataset on GitHub
job_creation_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Job_creation.xlsx'

# Load the dataset
Job_creation = pd.read_excel(job_creation_url, engine='openpyxl')
# Define income ranges for dropdown options
income_ranges = Job_creation['Income'].tolist()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for the income section
# Link to the dataset on GitHub
age_range_inc_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/IncAge_range.xlsx'

# Load the dataset
Age_rangeInc = pd.read_excel(age_range_inc_url, engine='openpyxl')
# Link to the dataset on GitHub
education_level_inc_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/IncEducation_level.xlsx'

# Load the dataset
Education_levelInc = pd.read_excel(education_level_inc_url, engine='openpyxl')
# Link to the dataset on GitHub
occupation_inc_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/IncOccupation.xlsx'

# Load the dataset
OccupationInc = pd.read_excel(occupation_inc_url, engine='openpyxl')
datasetsIncome = {
    'Age_range': Age_rangeInc,
    'Education_level':Education_levelInc,
    'Occupation': OccupationInc,
    
}
# Define dataset options for dropdown
dataset_options = [{'label': dataset, 'value': dataset} for dataset in datasetsIncome.keys()]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data and chart creation for the working time 
# Link to the dataset on GitHub
working_time_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/working_Time.xlsx'

# Load the dataset
workingTime = pd.read_excel(working_time_url, engine='openpyxl')
# Melt the DataFrame to have a tidy format
workingTime_melted = pd.melt(workingTime, id_vars=["Time"], var_name=["Location_Gender"], value_name="Population")

# Split the Location_Gender column into separate Location and Gender columns
workingTime_melted[['Location', 'Gender']] = workingTime_melted['Location_Gender'].str.split('_', expand=True)

# Create sunburst chart
figwork = px.sunburst(workingTime_melted, path=["Time", "Location", "Gender"], values="Population")

#-----------------------------------------------------------------------------Employment page layout-------------------------------------------------------------------------------------
layout = dbc.Container([
        html.Br(),
        html.Br(),
        html.H1('Employment',style={'textAlign':'center','fontSize': '30px','color': 'black','fontFamily':'Roboto Slab'},className='m-3'),
        html.Br(),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Population (16+) Employment Status by Different Categories", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center','border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}, 
        ),
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Select Category:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            # Dropdown for selecting dataset
                            dcc.Dropdown(
                                id="dropdown-1",
                                options=[
                                    {"label": "Age group", "value": "Age group"},
                                    {"label": "Economic activity", "value": "Economic activity"},
                                    {"label": "Occupation", "value": "Occupation"},
                                ],
                                value="Age group",  # Default selected value
                                style={
                                    'width': '80%',
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
                            ],className='m-2'),
                            # Dropdown for selecting dataset
                            dcc.Dropdown(
                                id="dropdown-2",
                                options=[
                                    {"label": "Gender", "value": "Gender"},
                                    {"label": "Residence", "value": "Residence"},
                                    {"label": "Agriculture", "value": "Agriculture"},
                                ],
                                value="Gender",  # Default selected value
                                style={
                                    'width': '80%',
                                    'textAlign': 'center',
                                    'fontSize': '15px',  # Adjust font size
                                    'borderRadius': '8px',  # Add rounded corners 
                                    },
                                clearable=False,
                                searchable=False,
                                className='m-2'
                            ),
                        ],width=6),
                    ]),
                    # Heatmap figure
                    dcc.Graph(id="heatmap"),
                ], style={'border': '2px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),               
            ],width=12),      
        ]),
        html.Br(),
        dbc.Row([
            html.Div(
                [
                    html.H3("Status in Employment for Employed Population by Different Categories", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
                ],
                style={'textAlign': 'center'}
            ),
#-------------------------------------------------------------------------------------------------------------------------------
            dbc.Col([
                html.Div([
                    #-----------------------
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Select Sector:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dcc.Dropdown(
                                id='datasectora',
                                options=[
                                    {'label': 'Formal Sector', 'value': 'formal_sector'},
                                    {'label': 'Informal Sector', 'value': 'informal_sector'},
                                    {'label': 'Formal Sector Out of Agriculture', 'value': 'formal_sector_out_of_agri'},
                                    {'label': 'Informal Sector Out of Agriculture', 'value': 'informal_sector_out_of_agri'}
                                ],
                                value='formal_sector',
                                style={
                                    'width': '70%',
                                    'textAlign': 'center',
                                    'fontSize': '15px',
                                    'borderRadius': '8px',
                                },
                                clearable=False,
                                searchable=False,
                                className='m-2'
                            ),
                        ]),
                    ]),
                    html.Br(),
                    html.Br(),
                    
                    #---------------------------
                    dbc.Row([
                        dbc.Col([
                            dcc.Checklist(
                                id='chectsector',
                                options=[
                                    {'label': 'Male', 'value': 'Male'},
                                    {'label': 'Female', 'value': 'Female'},
                                    {'label': 'Urban', 'value': 'Urban'},
                                    {'label': 'Rural', 'value': 'Rural'},
                                    {'label': 'In agriculture', 'value': 'In agriculture'},
                                    {'label': 'Not in agriculture', 'value': 'Not in agriculture'},
                                ],
                                value=['Male', 'Female', 'Urban', 'Rural', 'In agriculture', 'Not in agriculture'],  # Default selected values
                                inline=True,
                                className='m-2'
                            ),
                        ]),
                    ]),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Select Status:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dcc.Dropdown(
                                id='dropsector',
                                options=[
                                    {'label': 'Employee', 'value': 'Employee'},
                                    {'label': 'Employer', 'value': 'Employer'},
                                    {'label': 'Own-account worker', 'value': 'Own-account worker'},
                                    {'label': 'Member of cooperative', 'value': 'Member of cooperative'},
                                    {'label': 'Contributing family worker', 'value': 'Contributing family worker'},
                                ],
                                multi=True,  # Allow multiple selections
                                value=['Employee', 'Employer',  'Own-account worker', 'Member of cooperative', 'Contributing family worker' ],  # Default selected values
                                style={
                                    'width': '70%',
                                    'textAlign': 'center',
                                    'fontSize': '15px',
                                    'borderRadius': '8px',
                                },
                                clearable=False,
                                searchable=False,
                                className='m-2'
                            ),
                        ]),
                    ]),
                ], className='m-2',style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
            ], width=6),
            dbc.Col([
                html.Div([
                    dcc.Graph(id='spidersectorf'),
                ], className='m-2'),
            ], width=6),
            

#-------------------------------------------------------------------------------------------------------------------------------
        ]),
        html.Br(),
        dbc.Row([
            html.Div(
                [
                    html.H3("Monthly Income from Employment of Employees at Main Job", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
                ],
                style={'textAlign': 'center'}
            ),
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3("Employed Population Percentages by Amount of Income", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}
                    ),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    html.Div([
                        html.H3("Select Income Range:",style={'fontSize':'16px'})
                    ],className='m-2'),
                    # Dropdown for selecting income range
                    dcc.Dropdown(
                        id='income-dropdown',
                        options=[{'label': income, 'value': income} for income in income_ranges],
                        value=income_ranges[0],  # Default selected value
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
                    dbc.Row([
                        dbc.Col(
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div(id='total-value', style={'fontSize': '20px','color': 'black'}),
                                    html.Div("Employed Persons", style={'fontSize': '16px','color': 'black'}),
                                ],className="border-start border-info border-5")
                            ],className="text-center m-2"),
                            width=5),
                    ], justify='center'),                
                    # Gauges for percentages in the same row
                    html.Div([
                        # Rwanda Gauge
                        html.Div([
                            html.H4("Pop % in Rwanda", style={'textAlign': 'center'}),
                            html.Br(),
                            dcc.Graph(id='rwanda-gauge', figure={}),
                        ], style={'flex': '0.4'}),
                        
                        # Urban Gauge
                        html.Div([
                            html.H4("Pop % in Urban Areas", style={'textAlign': 'center'}),
                            html.Br(),
                            dcc.Graph(id='urban-gauge', figure={}),
                        ], style={'flex': '0.4'}),
                        
                        # Rural Gauge
                        html.Div([
                            html.H4("Pop % in Rural Areas", style={'textAlign': 'center'}),
                            html.Br(),
                            dcc.Graph(id='rural-gauge', figure={}),
                        ], style={'flex': '0.4'}),
                    ], style={'display': 'flex', 'justifyContent': 'space-around', 'margin-top': '10px'}), 
                ], style={'border': '2px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}
                ),
                               
            ],width=8),
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3('Working Time For Employed Population by Residence/Gender ', style={'color': 'black','textAlign':'center', 'margin': '0 auto'}),
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    dcc.Graph(figure=figwork),
                ], style={'border': '2px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
            ], width=4)

        ]),
        html.Br(),
        dbc.Row([
            # html.Div(
            #     [
            #         html.H3("Incomes from employment ", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            #     ],
            #     style={'textAlign': 'center'}
            # ),

            html.Div([
                html.H3('Incomes From Employment by Different Categories ', style={'color': 'black','textAlign':'center', 'margin': '0 auto'}),
            ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
            html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3("Select Category:",style={'fontSize':'16px'})
                    ],className='m-2'),
                # Dropdown for selecting dataset
                dcc.Dropdown(
                    id='dataset-dropdown',
                    options=dataset_options,
                    value=list(datasetsIncome.keys())[0],  # Default selected value
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

                # Stacked bar chart
                dcc.Graph(id='stacked-bar-chart')
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
            ],width=12),
        ]),
        html.Br(),
    ],
    fluid=True
)
#----------------------------------------------------------------------------------Callback section-----------------------------------------------------------
# Callback to update heatmap based on selected dataset
@callback(
    Output("heatmap", "figure"),
    [Input("dropdown-1", "value"), Input("dropdown-2", "value")],
)
def update_heatmap(selected_option, selected_option_2):
    # print(f"selected_option: {selected_option}, selected_option_2: {selected_option_2}")

    # Handle invalid selected_option values
    if selected_option not in ["Age group", "Economic activity", "Occupation"]:
        # print("Error: Invalid selection for 'selected_option':", selected_option)
        return {}

    # Retrieve data based on selected_option
    if selected_option == "Age group":
        data = age_range_df
    elif selected_option == "Economic activity":
        data = economic_activity_df
    elif selected_option == "Occupation":
        data = occupation_df

    # Handle invalid selected_option_2 values
    if selected_option_2 == "Gender":
        z_data = data[["Male", "Female"]].values.T
        y_data = ["Male", "Female"]
    elif selected_option_2 == "Residence":
        z_data = data[["Urban", "Rural"]].values.T
        y_data = ["Urban", "Rural"]
    elif selected_option_2 == "Agriculture":
        z_data = data[["In agriculture", "Not in agriculture"]].values.T
        y_data = ["In agriculture", "Not in agriculture"]
    else:
        # print("Error: Invalid selection for 'selected_option_2':", selected_option_2)
        return {}
    # Wrap x-axis labels using textwrap.wrap
    wrapped_labels = [textwrap.wrap(label, 20)[0] for label in data["Category"]]

    # Generate heatmap plot
    fig = go.Figure(go.Heatmap(z=z_data, x=wrapped_labels, y=y_data, colorscale="viridis"))
    fig.update_layout(title_text="Heatmap")
    return fig
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Callback to update card and gauges based on selected income range for the income section
@callback(
    [Output('total-value', 'children'),
     Output('rwanda-gauge', 'figure'),
     Output('urban-gauge', 'figure'),
     Output('rural-gauge', 'figure')],
    [Input('income-dropdown', 'value')]
)
def update_display(selected_income):
    # Filter DataFrame based on selected income range
    selected_row = Job_creation[Job_creation['Income'] == selected_income].squeeze()

    # Update card with total value
    total_value = selected_row['Total']

    # Update gauges with percentage values
    rwanda_percentage = selected_row['Rwanda']
    urban_percentage = selected_row['Urban']
    rural_percentage = selected_row['Rural']

    # Create gauge figures
    rwanda_fig = create_gauge('Rwanda', rwanda_percentage)
    urban_fig = create_gauge('Urban', urban_percentage)
    rural_fig = create_gauge('Rural', rural_percentage)

    return total_value, rwanda_fig, urban_fig, rural_fig

# Function to create a gauge figure
def create_gauge(label, value):
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': label, 'font': {'size': 14}},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "darkblue"},
               'bgcolor': "white",
               'borderwidth': 2,
               'bordercolor': "gray",
               'steps': [{'range': [0, 100], 'color': "lightgray"}],
            #    'threshold': {'line': {'color': "red", 'width': 2}, 'thickness': 0.75, 'value': 60}
               }))

    fig.update_layout(height=150, margin=dict(l=10, r=10, t=10, b=10))
    return fig
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update the stacked bar chart based on selected dataset
@callback(
    Output('stacked-bar-chart', 'figure'),
    [Input('dataset-dropdown', 'value')]
)
def update_stacked_bar_chart(selected_dataset):
    selected_data = datasetsIncome[selected_dataset]

    fig = go.Figure()

    for column in ['Urban', 'Rural']:
        wrapped_labels = [textwrap.wrap(label, 20)[0] for label in selected_data['Category']]
        fig.add_trace(go.Bar(
            x=wrapped_labels,
            y=selected_data[column],
            name=column,
            marker_color='rgb(26, 118, 255)' if column == 'Urban' else 'rgb(55, 83, 109)',
        ))

    fig.update_layout(
        barmode='group',
        xaxis_title=f'{selected_dataset}',
        yaxis_title='Income(in Rwf)',
        showlegend=True,
        legend=dict(x=1, y=1.0, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
    )

    # Add centered title above the chart
    fig.update_layout(annotations=[
        dict(
            xref='paper',
            yref='paper',
            x=0.5,
            y=1.15,
            text=f'Average Monthly Income by {selected_dataset}',
            showarrow=False,
            font=dict(size=16, color='black'),
            align='center'
        )
    ])

    return fig

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
@callback(
    Output('spidersectorf', 'figure'),
    [Input('datasectora', 'value'),
     Input('dropsector', 'value'),
     Input('chectsector', 'value')]
)
def update_spider_chart(selected_dataset, selected_variables, enabled_categories):
    # Select the appropriate dataset based on user input
    if selected_dataset == 'formal_sector':
        df = formal_sector
    elif selected_dataset == 'informal_sector':
        df = informal_sector
    elif selected_dataset == 'formal_sector_out_of_agri':
        df = formal_sector_out_of_agri
    elif selected_dataset == 'informal_sector_out_of_agri':
        df = informal_sector_out_of_agri

    # Create spider chart
    fig = go.Figure()

    for category in enabled_categories:
        values = df[df['Status'] == category][selected_variables].values.flatten()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=selected_variables,
            name=category
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(df[selected_variables].values.flatten())]
            )
        ),
        showlegend=True
    )

    return fig