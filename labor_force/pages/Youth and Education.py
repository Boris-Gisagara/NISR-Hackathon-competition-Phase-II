import dash
import dash_bootstrap_components as dbc
from dash import dcc, html,callback
import dash.dependencies as dd
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
dash.register_page(__name__, path='/Youth&Education')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Labor Forcee sunburst
# Link to the dataset on GitHub
youth_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Youth.xlsx'

# Load the dataset
dfSun = pd.read_excel(youth_url, engine='openpyxl')
#Scatter plot for NEET
# Link to the dataset on GitHub
neet_age_range_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Neetage_range.xlsx'

# Load the dataset
df_youth_age = pd.read_excel(neet_age_range_url, engine='openpyxl')

# Link to the dataset on GitHub
neet_education_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Neeteducation.xlsx'

# Load the dataset
df_educational_level = pd.read_excel(neet_education_url, engine='openpyxl')

# Sample data for NEET
EdField = {
    'Field': ['General program', 'Education', 'Humanities and arts', 'Social sciences, business and law', 'Science', 'Engineering, manufacturing and construction', 'Agriculture', 'Health and welfare', 'Services', 'No Education'],
    'Total': [5596521, 145570, 111448, 303031, 506331, 173683, 45989, 66434, 57432, 957147]
}
#data for the second card Tchnical training
# Link to the dataset on GitHub
tech_training_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/Technical%20training.xlsx'

# Load the dataset
TechT = pd.read_excel(tech_training_url, engine='openpyxl')
# Dropdown options
dropdown_options_tech = [{'label': skill, 'value': skill} for skill in TechT['Technical skills']]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# the dataset for the radar chart on the education attainment
# Link to the dataset on GitHub
education_attainment_url = 'https://github.com/Boris-Gisagara/NISR-Hackathon-competition-Phase-II/raw/main/labor_force/dataset/education_attainment.xlsx'

# Load the dataset
EdAtt = pd.read_excel(education_attainment_url, engine='openpyxl')
# Create a spider chart
figSpid = go.Figure()

for index, row in EdAtt.iterrows():
    figSpid.add_trace(go.Scatterpolar(
        r=row[["Male", "Female", "Urban", "Rural", "In agriculture", "Not in agriculture", "Male"]].tolist(),  # Close the loop
        theta=["Male", "Female", "Urban", "Rural", "In agriculture", "Not in agriculture", "Male"],  # Close the loop       
        name=row["Level"]
    ))

figSpid.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, EdAtt[["Male", "Female", "Urban", "Rural", "In agriculture", "Not in agriculture"]].max().max()],
            showgrid=True,       # Show the radial grid lines
            gridwidth=1,         # Set the width of the grid lines
            gridcolor='#233336'    # Set the color of the grid lines to black
        )
    )
)
#----------------------------------------------------------------------------------------youth and education page layout -------------------------------------------------------------------------------------------
layout = dbc.Container([
        html.Br(),
        html.Br(),
        html.H1('Youth and Education',style={'textAlign':'center','fontSize': '30px','color': 'black','fontFamily':'Roboto Slab'},className='m-3'),
        html.Br(),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("Youth Employment Status in Rwanda & Field of study/Technical training ", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3("Youth/Young Population by Gender/Residence/In&Not in Agriculture", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px','textAlign': 'center'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),   
                    html.Div([
                        html.H3("Select Category:",style={'fontSize':'16px'})
                    ],className='m-2'),
                    dcc.Dropdown(
                        id='category-dropdown',
                        options=[
                            {'label': 'Gender', 'value': 'Gender'},
                            {'label': 'Residence', 'value': 'Residence'},
                            {'label': 'Agriculture', 'value': 'Agriculture'}
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
                    dcc.Graph(id='sunburst-chart')
                ],style={'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc','backgroundColor':'white'}),  
            ],width=6),
            dbc.Col([
                html.Div([
                #card 1---------------------------------------------------------------------------------------------------------------------------------------------------------- 
                html.Div([
                    html.H3("Population (16+) by field of education", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                ],className="border-start border-primary border-5 m-4", style={'height': '40px','textAlign': 'center'}),
                html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}), 
                html.Br(),
                html.Div([
                    html.H3("Select Field:",style={'fontSize':'16px'})
                ],className='m-2'),
                dcc.Dropdown(
                    id='field-dropdown',
                    options=[{'label': field, 'value': field} for field in EdField['Field']],
                    value='General program',
                    style={
                        'width': '70%',
                        'textAlign': 'center',
                        'fontSize': '15px',  # Adjust font size
                        'borderRadius': '8px',  # Add rounded corners 
                           },  # Add margin-bottom for space
                    clearable=False,
                    searchable=False,
                    className='m-2'
                ),
                html.Br(),
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody([
                                    html.P(id='card-output', className="card-text text-center", style={'textAlign': 'center', 'fontSize': '25px'}),
                                ],className="border-start border-info border-5"),
                                className="mb-3 m-2",
                                style={'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc','width':'100%','backgroundColor':'white'}  # Increased boxShadow size
                            ),
                        ],width=6)
                    ], justify='left')
                ]),
                
                #card 2----------------------------------------------------------------------------------------------------------------------------------------------------------   
                html.Div([
                    html.H3("Population (16+) by Technical Training", style={'fontSize':'20px','color': 'black','textAlign':'center', 'margin': '0 auto'})
                ],className="border-start border-primary border-5 m-4", style={'height': '40px','textAlign': 'center'}),
                html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}), 
                html.Br(),
                html.Div([
                    html.H3("Select Technical trainig:",style={'fontSize':'16px'})
                ],className='m-2'),             
                dcc.Dropdown(
                    id='tech-dropdown',
                    options=dropdown_options_tech,
                    value=dropdown_options_tech[0]['value'],  # Initial value
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
                html.Br(),
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody([
                                    # html.H4("Technical Training", className="card-title text-center", style={'textAlign': 'center', 'fontSize': '20px'}),
                                    html.P(id='tech-total-counts', className="card-text text-center", style={'textAlign': 'center', 'fontSize': '25px'}),
                                ],className="border-start border-info border-5"),
                                className="mb-3 m-2",
                                style={'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc','width':'100%','backgroundColor':'white'},  # Increased boxShadow size
                                # className="text-center m-4"
                            )
                        ],width=6)
                    ], justify='left')
                ]),
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)','backgroundColor':'white','borderRadius': '15px'}),
            ],width=6,className="mx-auto")
        ]),
        html.Br(),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        dbc.Row([
            html.Div(
                [
                    html.H3("Youth NEET (Not in Employment, Education, or Training and Education Attainment", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
                ],
                style={'textAlign': 'center'}
            ),
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3('Youth Population NEET', style={'color': 'black','textAlign':'center', 'margin': '0 auto'}),
                ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),

                html.Div([
                    html.H3("Select Category:",style={'fontSize':'16px'})
                ],className='m-2'),
                dcc.Dropdown(
                    id='neetsundro',
                    options=[
                        {'label': 'Youth Age Range', 'value': 'youth_age'},
                        {'label': 'Educational Level', 'value': 'educational_level'}
                    ],
                    value='youth_age',  # Default selected value
                    className='m-2',
                    style={'width': '80%'}

                ),
                
                # Sunburst Graph
                dcc.Graph(id='neetsun')




                      
                ],style={'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc','backgroundColor':'white'}),         
            ],width=6),



            dbc.Col([
                html.Div([
                html.Div([
                    html.H3('Youth Population by Education Attainment', style={'color': 'black','textAlign':'center', 'margin': '0 auto'}),
                ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                dcc.Graph(figure=figSpid)
                ],style={'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)','border': '2px solid #ccc','backgroundColor':'white'}),
            ],width=6)


        ]),
        html.Br(),
    ],
    fluid=True
)
#-------------------------------------------------------------------------------------Callback section----------------------------------------------------------------------------------------------
# Callback to update the total counts based on the selected technical skill 
@callback(
    Output('tech-total-counts', 'children'),
    [Input('tech-dropdown', 'value')]
)
def update_tech_total_counts(selected_skill):
    total_counts = TechT[TechT['Technical skills'] == selected_skill]['Total'].values[0]
    return f"{total_counts} Persons"
#------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update card text based on dropdown selection for field of education
@callback(
    Output('card-output', 'children'),
    [Input('field-dropdown', 'value')]
)
def update_card(selected_field):
    total_count = EdField['Total'][EdField['Field'].index(selected_field)]
    return f"{total_count:,} Persons"
#------------------------------------------------------------------------------------------------------------------------------------------
# Define callback to update the chart(sunburst) for youth population based on dropdown selection
@callback(
    Output('sunburst-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_sunburst_chart(selected_category):
    # Update the chart based on the selected category
    if selected_category == 'Gender':
        fig = px.sunburst(data_frame=dfSun, path=['Status', 'Age Group', 'Gender'], values='Gpop', color='Age Group')
    elif selected_category == 'Residence':
        fig = px.sunburst(data_frame=dfSun, path=['Status', 'Age Group', 'Residence'], values='Rpop', color='Age Group')
    elif selected_category == 'Agriculture':
        fig = px.sunburst(data_frame=dfSun, path=['Status', 'Age Group', 'Agriculture'], values='Apop', color='Age Group')
    else:
        # Default to Gender if the selected category is not recognized
        fig = px.sunburst(data_frame=dfSun, path=['Status', 'Age Group', 'Gender'], values='Gpop')

    return fig
#------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to update the Sunburst graph based on the selected dataset
@callback(
    Output('neetsun', 'figure'),
    [Input('neetsundro', 'value')]
)
def update_graph(selected_dataset):
    if selected_dataset == 'youth_age':
        fig = px.sunburst(df_youth_age, path=['age_range', 'Residence', 'Gender'], values='Population',
                          color='Residence', color_discrete_map={'Urban': 'lightblue', 'Rural': 'lightgreen'},
                          branchvalues='total')
        fig.update_layout(title_text='Youth Not employed, Not educational and Not training (NEET) - Age range')
    else:
        fig = px.sunburst(df_educational_level, path=['Educational_level', 'Residence', 'Gender'], values='Population',
                          color='Residence', color_discrete_map={'Urban': 'lightblue', 'Rural': 'lightgreen'},
                          branchvalues='total')
        fig.update_layout(title_text='Youth Not employed, Not educational and Not training (NEET) - educational level')

    return fig
#------------------------------------------------------------------------------------------------------------------------------------------------
