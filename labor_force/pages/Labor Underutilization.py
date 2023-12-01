import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc,html, callback
import dash.dependencies as dd
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output
#----------------------------------------------------------------------------------------------------------------------------------------------------------------


dash.register_page(__name__, path='/Labor_Underutilization')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load the data for unemployment population 
# Link to the dataset on GitHub
unemployment_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/unemployment.xlsx'

# Load the dataset
dfUnempl = pd.read_excel(unemployment_url, engine='openpyxl')
# Load the data for underutilization by age group
# Link to the dataset on GitHub
underutilization1_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/underutilizatoin1.xlsx'

# Load the dataset
dfunder1 = pd.read_excel(underutilization1_url, engine='openpyxl')
# Load the data for underutilization by underutilisation
# Link to the dataset on GitHub
underutilization2_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/underutilization2.xlsx'

# Load the dataset
dfUnder2 = pd.read_excel(underutilization2_url, engine='openpyxl')
# Load the dataset for self reported status
# Link to the dataset on GitHub
selfRep_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/selfRep.xlsx'

# Load the dataset
selfRep = pd.read_excel(selfRep_url, engine='openpyxl')
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Load the data for livelihood source
# Link to the dataset on GitHub
livelihood_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/livelihoodSource.xlsx'

# # Load the dataset
livelihood = pd.read_excel(livelihood_url, engine='openpyxl')
# Melt the dataframe to reshape it for plotting
livelihood_melted = pd.melt(livelihood, id_vars='Source', var_name='Category', value_name='Population')
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Load the dataset for donut chart on reasond for being out of labor force
# Link to the dataset on GitHub
reasons_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/ReasonsOut.xlsx'

# Load the dataset
Reasons = pd.read_excel(reasons_url, engine='openpyxl')
#---------------------------------------------------------------------------------Unemplyment page layout-------------------------------------------------------------------------------
# load the data for unemployment
# Link to the dataset on GitHub
age_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/unemploymentAge.xlsx'

# Load the dataset
df_age = pd.read_excel(age_url, engine='openpyxl')

# Link to the dataset on GitHub
edu_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/unemploymentEdu.xlsx'

# Load the dataset
df_edu = pd.read_excel(edu_url, engine='openpyxl')
#---------------------------------------------------------------------------------Unemplyment page layout-------------------------------------------------------------------------------
# Link to the dataset on GitHub
outside_lf_cate_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/OutSideLFcate.xlsx'

# Load the dataset
dataFliveli = pd.read_excel(outside_lf_cate_url, engine='openpyxl')
#---------------------------------------------------------------------------------Unemplyment page layout-------------------------------------------------------------------------------
# Link to the dataset on GitHub
outlf_reason_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/out%20side%20LF.xlsx'

# Load the dataset
OutLFReason = pd.read_excel(outlf_reason_url, engine='openpyxl')
#---------------------------------------------------------------------------------Unemplyment page layout-------------------------------------------------------------------------------
layout = dbc.Container([
        html.Br(),
        html.Br(),
        html.H1('Labor Underutilization',style={'textAlign':'center','fontSize': '30px','color': 'black','fontFamily':'Roboto Slab'},className='m-3'),
        html.Br(),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Unemployed population by Age Group/Education Level", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3("Select Category:",style={'fontSize':'16px'})
                    ],className='m-2'),
                    # Dropdown for Gender, Residence, and Status in agriculture
                    dcc.Dropdown(
                        id='dropdown-unemployment',
                        options=[
                            {'label': 'Gender', 'value': 'Gender'},
                            {'label': 'Residence', 'value': 'Residence'},
                            {'label': 'Status in Agriculture', 'value': 'Agriculture'}
                        ],
                        value='Gender',
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
                ],width=4),
                dbc.Col([
                    html.Div([
                        html.H3("Select Category:",style={'fontSize':'16px'})
                    ],className='m-2',style={'textAlign': 'center'}),
                    dbc.Form([
                        html.Div([
                            # Radio button for Age range or Education Attained
                            dbc.RadioItems(
                                id='radio-unemployment',
                                options=[
                                    {'label': 'Age Range', 'value': 'Age range'},
                                    {'label': 'Education Attained', 'value': 'Education'}
                                ],
                                value='Age range',
                                inline=True,
                                labelStyle={'display': 'block'},
                                className='custom-radio m-2',
                                style={'textAlign': 'center'}
                            ),
                        ]),
                    ]),
                ],width=4)
            ]),
            # Bar chart to be updated
            dcc.Graph(id='bar-unemployment'),
        ],style={'border': '2px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
        html.Br(),
#---------------------------------------------------------------------------------Unemplyment page layout-------------------------------------------------------------------------------
#section two
        dbc.Row([
            html.Div(
                [
                    html.H3("Time Related Underemployment", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
                ],
                style={'textAlign': 'center'}
                ),
                dbc.Col([
                    dbc.Form([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.H3("Choose category:",style={'fontSize':'16px'})
                                ],className='m-2',style={'textAlign': 'center'}),
                                dbc.RadioItems(
                                    id='toggle-radio',
                                    options=[
                                        {'label': 'Gender', 'value': 'gender'},
                                        {'label': 'Residence', 'value': 'residence'}
                                    ],
                                    value='gender',
                                    labelStyle={'display': 'inline-block', 'margin-right': '10px'},
                                    inline=True,
                                    className='custom-radio m-2',
                                    style={'textAlign': 'center'}
                                ),
                            ],className='m-4',style={'width': '400px', 'border': '1px solid #ccc', 'border-top': 'none', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
                            dcc.Graph(id='pyramid-chart')
                        ],style={'border': '2px solid #ccc'}),
                    ]),
                    
                ],width=7),
                dbc.Col([
                    html.Div([
                        html.H3("Time-related underemployment by branches of economic activities", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px','textAlign': 'center'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    html.Br(),
                    html.Br(),
                    html.Div([
                        html.H3("Select Status:",style={'fontSize':'16px'})
                    ],className='m-2'),
                        dcc.Dropdown(
                            id='isic-dropdown',
                            options=[{'label': i, 'value': i} for i in dfUnder2['ISIC High level'].unique()],
                            value=dfUnder2['ISIC High level'].unique()[0],
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
                        html.Br(),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                html.H4("Male Counts"),
                                html.P(id='male-count', style={'fontSize': '20px'})
                                ],className="border-start border-info border-5")
                            ], style={'margin': '10px', 'border': '2px solid #ccc', 'width': 'auto'})
                            ]),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody([
                                    html.H4("Female Counts"),
                                    html.P(id='female-count', style={'fontSize': '20px'})
                                    ],className="border-start border-info border-5")
                                ], style={'margin': '10px', 'border': '2px solid #ccc', 'width': 'auto'})
                            ])
                        ], justify='center'),
                        dbc.Row([
                            dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                html.H4("Urban Counts"),
                                html.P(id='urban-count', style={'fontSize': '20px'})
                                ],className="border-start border-info border-5")
                            ], style={'margin': '10px', 'border': '2px solid #ccc', 'width': 'auto'})
                            ]),
                            dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                html.H4("Rural Counts"),
                                html.P(id='rural-count', style={'fontSize': '20px'})
                                ],className="border-start border-info border-5")
                            ], style={'margin': '10px', 'border': '2px solid #ccc', 'width': 'auto'})
                            ])
                        ], justify='center')
                ], width=5)
        ]),
        html.Br(),
        dbc.Row([
            html.Div(
                [
                    html.H3("Population outside the labour force", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
                ],
                style={'textAlign': 'center'}
            ),
            dbc.Col([
                html.H3("Self Reported Status:", style={'fontSize': '20px', 'textAlign': 'left'}),
                dcc.Dropdown(
                    id='status-dropdown',
                    options=[
                        {'label': status, 'value': status} for status in selfRep['Status']
                    ],
                    value=selfRep['Status'][0],  # Default selected option
                    style={
                        'width': '60%',
                        'textAlign': 'center',
                        'fontSize': '15px',  # Adjust font size
                        'borderRadius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False,
                    className='m-2'
                ),
                html.Br(),
                html.Br(),
                html.Div([                
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Male", style={'textAlign': 'center', 'fontSize': '20px'},className="border-start border-info border-5"),
                            dbc.CardBody(id='male-card', style={'textAlign': 'center', 'fontSize': '25px'},className="border-start border-info border-5"),
                        ],style={'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),
                    ], width=3),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Female", style={'textAlign': 'center', 'fontSize': '20px'},className="border-start border-info border-5"),
                            dbc.CardBody(id='female-card', style={'textAlign': 'center', 'fontSize': '25px'},className="border-start border-info border-5"),
                        ],style={'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),
                    ], width=3),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Urban", style={'textAlign': 'center', 'fontSize': '20px'},className="border-start border-info border-5"),
                            dbc.CardBody(id='urban-card', style={'textAlign': 'center', 'fontSize': '25px'},className="border-start border-info border-5"),
                        ],style={'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),
                    ], width=3),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader("Rural", style={'textAlign': 'center', 'fontSize': '20px'},className="border-start border-info border-5"),
                            dbc.CardBody(id='rural-card', style={'textAlign': 'center', 'fontSize': '25px'},className="border-start border-info border-5"),
                        ],style={'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc'}),
                    ], width=3),
                ]),
            ], 
            style={'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
            ],width=12),
        ]),
        html.Br(),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

        dbc.Row([
            html.Div(
                [
                    html.H3("Population outside the labour force", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
                ],
                style={'textAlign': 'center'}
            ),
            dbc.Col([
                html.Div([
                    dbc.Row([
                        html.Div([
                            html.H3("Population Distribution by Main Source of Livelihood", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                            ],className="border-start border-primary border-5 m-4", style={'height': '40px'}
                        ),
                        dbc.Col([
                            html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                            html.Div([
                                html.H3("Select Source:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dcc.Dropdown(
                                id='categoryreos',
                                options=[{'label': category, 'value': category} for category in dataFliveli['Category of outside labor force']],
                                value=dataFliveli['Category of outside labor force'][0],
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
                        ],width=6),
                        dbc.Col([
                            html.Div([
                                html.H3("Select Category:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dcc.Dropdown(
                                id='comporeos',
                                options=[
                                    {'label': 'Gender', 'value': 'Gender'},
                                    {'label': 'Residence', 'value': 'Residence'},
                                    {'label': 'Agriculture Status', 'value': 'Agriculture Status'}
                                ],
                                value='Gender',  # Default selected option
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
                        ],width=6),
                    ]),
                    dcc.Graph(id='donutreos'),  # Updated to bar chart
                ], style={'border': '2px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
            ], width=6),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3("Potential Labor Force", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                        ],className="border-start border-primary border-5 m-4", style={'height': '40px'}
                    ),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Select Reasaon:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dcc.Dropdown(
                                id='potereasondrop',
                                options=[{'label': reason, 'value': reason} for reason in OutLFReason['Reasons']],
                                value=OutLFReason['Reasons'][0],
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
                        ],width=6),
                        dbc.Col([
                            html.Div([
                                html.H3("Select Category:",style={'fontSize':'16px'})
                            ],className='m-2'),
                            dcc.Dropdown(
                                id='potecategdrop',
                                options=[
                                    {'label': 'Gender', 'value': 'Gender'},
                                    {'label': 'Residence', 'value': 'Residence'},
                                    {'label': 'Agriculture Status', 'value': 'Agriculture Status'}
                                ],
                                value='Gender',
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
                        ],width=6),
                    ]),                    
                    dcc.Graph(id='potereodonut'),
                ], style={'backgroundColor':'white','border': '2px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white'}),
            ], width=6),
        ]),
        html.Br(),
    ],
fluid=True
)
#--------------------------------------------------------------------------Callback setion----------------------------------------------------------------------
# Callback to update the bar chart based on radio button and dropdown selection
@callback(
    Output('bar-unemployment', 'figure'),
    [Input('radio-unemployment', 'value'),
     Input('dropdown-unemployment', 'value')]
)
def update_bar_chart(selected_radio, selected_dropdown):
    # Select the appropriate DataFrame based on the radio button selection
    if selected_radio == 'Age range':
        df = df_age
    elif selected_radio == 'Education':
        df = df_edu
    else:
        return {}  # Invalid option, return an empty figure
    
    # Select the y values based on the dropdown selection
    if selected_dropdown == 'Gender':
        y_values = ['Male', 'Female']
    elif selected_dropdown == 'Residence':
        y_values = ['Urban', 'Rural']
    elif selected_dropdown == 'Agriculture':
        y_values = ['In agriculture', 'Not in agriculture']
    else:
        return {}  # Invalid option, return an empty figure
    
    # Create the bar chart
    fig = {
        'data': [
            {'x': df['Categories'], 'y': df[y], 'type': 'bar', 'name': y} for y in y_values
        ],
        'layout': {
            'barmode': 'group',
            'title': f' Unemployed Population by {selected_radio} and {selected_dropdown}',
            'xaxis': {'title': selected_radio},
            'yaxis': {'title': 'Count'},
        }
    }

    return fig
#------------------------------------------------------------------------------------------------------------------------------------------------
# Define the callback to update the chart based on the radio button selection
@callback(
    Output('pyramid-chart', 'figure'),
    [Input('toggle-radio', 'value')]
)
def update_pyramid_chart(selected_option):
    if selected_option == 'gender':
        labels = ['16-24 yrs', '25-34 yrs', '35-54 yrs', '55-64 yrs', '65+ yrs']
        male_data = dfunder1['Male'].tolist()
        female_data = [-1 * value for value in dfunder1['Female'].tolist()]  # Negative values for females
        title = 'Time related under employment by Age Group/Gender'
    else:
        labels = ['16-24 yrs', '25-34 yrs', '35-54 yrs', '55-64 yrs', '65+ yrs']
        urban_data = dfunder1['Urban'].tolist()
        rural_data = [-1 * value for value in dfunder1['Rural'].tolist()]  # Negative values for rural
        title = 'Time related under employment by Age Group/Residence area'

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=labels,
        x=male_data if selected_option == 'gender' else urban_data,
        orientation='h',
        name='Male' if selected_option == 'gender' else 'Urban',
        marker=dict(color='#e8422c')
    ))

    fig.add_trace(go.Bar(
        y=labels,
        x=female_data if selected_option == 'gender' else rural_data,
        orientation='h',
        name='Female' if selected_option == 'gender' else 'Rural',
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
#------------------------------------------------------------------------------------------------------------------------------------------------
# Define the callback to update the cards based on the dropdown selection
@callback(
    [Output('male-count', 'children'),
     Output('female-count', 'children'),
     Output('urban-count', 'children'),
     Output('rural-count', 'children')],
    [Input('isic-dropdown', 'value')]
)
def update_cards(selected_option):
    filtered_df = dfUnder2[dfUnder2['ISIC High level'] == selected_option]

    male_count = f"Total: {filtered_df['Male'].values[0]:,}"
    female_count = f"Total: {filtered_df['Female'].values[0]:,}"
    urban_count = f"Total: {filtered_df['Urban'].values[0]:,}"
    rural_count = f"Total: {filtered_df['Rural'].values[0]:,}"

    return male_count, female_count, urban_count, rural_count
#------------------------------------------------------------------------------------------------------------------------------------------------
# Define callback to update card values
@callback(
    [Output('male-card', 'children'),
     Output('female-card', 'children'),
     Output('urban-card', 'children'),
     Output('rural-card', 'children')],
    [Input('status-dropdown', 'value')]
)
def update_cards(selected_status):
    selected_data = selfRep[selfRep['Status'] == selected_status]

    male_value = selected_data['Male'].values[0]
    female_value = selected_data['Female'].values[0]
    urban_value = selected_data['Urban'].values[0]
    rural_value = selected_data['Rural'].values[0]

    return f"{male_value:,}", f"{female_value:,}", f"{urban_value:,}", f"{rural_value:,}"

#-------------------------------------------------------------------------------------------------------
@callback(
    Output('donutreos', 'figure'),
    [
        Input('categoryreos', 'value'),
        Input('comporeos', 'value'),
    ]
)
def update_donut_chart(selected_category, selected_comparison):
    filtered_data = dataFliveli[dataFliveli['Category of outside labor force'] == selected_category]

    if selected_comparison == 'Gender':
        labels = ['Male', 'Female']
        values = [
            filtered_data['Male'].values[0] if 'Male' in filtered_data.columns else 0,
            filtered_data['Female'].values[0] if 'Female' in filtered_data.columns else 0
        ]
    elif selected_comparison == 'Residence':
        labels = ['Urban', 'Rural']
        values = [
            filtered_data['Urban'].values[0] if 'Urban' in filtered_data.columns else 0,
            filtered_data['Rural'].values[0] if 'Rural' in filtered_data.columns else 0
        ]
    elif selected_comparison == 'Agriculture Status':
        labels = ['In agriculture', 'Not in agriculture']
        values = [
            filtered_data['In agriculture'].values[0] if 'In agriculture' in filtered_data.columns else 0,
            filtered_data['Not in agriculture'].values[0] if 'Not in agriculture' in filtered_data.columns else 0
        ]

    figLiveli = px.pie(values=values, names=labels, hole=0.4, title=f'{selected_category} by {selected_comparison}')
    return figLiveli
#-------------------------------------------------------------------------------------------------------
# Define callback to update donut chart based on user input
@callback(
    Output('potereodonut', 'figure'),
    [
        Input('potereasondrop', 'value'),
        Input('potecategdrop', 'value'),
    ]
)
def update_donut_chart(selected_reason, selected_category):
    filtered_data = OutLFReason[OutLFReason['Reasons'] == selected_reason]

    if selected_category == 'Gender':
        labels = ['Male', 'Female']
        values = [
            filtered_data['Male'].values[0] if 'Male' in filtered_data.columns else 0,
            filtered_data['Female'].values[0] if 'Female' in filtered_data.columns else 0
        ]
    elif selected_category == 'Residence':
        labels = ['Urban', 'Rural']
        values = [
            filtered_data['Urban'].values[0] if 'Urban' in filtered_data.columns else 0,
            filtered_data['Rural'].values[0] if 'Rural' in filtered_data.columns else 0
        ]
    elif selected_category == 'Agriculture Status':
        labels = ['In agriculture', 'Not in agriculture']
        values = [
            filtered_data['In agriculture'].values[0] if 'In agriculture' in filtered_data.columns else 0,
            filtered_data['Not in agriculture'].values[0] if 'Not in agriculture' in filtered_data.columns else 0
        ]

    fig = px.pie(values=values, names=labels, hole=0.4, title=f'{selected_reason} - {selected_category}')
    return fig