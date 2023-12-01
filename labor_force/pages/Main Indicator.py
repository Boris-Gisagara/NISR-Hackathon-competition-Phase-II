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
dfrate = pd.read_excel(r"C:\Users\user\OneDrive\Documents\python works\labor_force\dataset\indicator-Age.xlsx")

EduIndicator = pd.read_excel(r"C:\Users\user\OneDrive\Documents\python works\labor_force\dataset\edu_levelrate.xlsx")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
Econoagri= pd.read_excel(r"C:\Users\user\OneDrive\Documents\python works\labor_force\dataset\Econoagri.xlsx")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load the dataset for employed population IN/NOT in agriculture
employ_agri = pd.read_excel(r"C:\Users\user\OneDrive\Documents\python works\labor_force\dataset\EmployAgri.xlsx")
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
# Load the dataset for tained populatiion in agriculture and not in agriculture
training_data = pd.read_excel(r"C:\Users\user\OneDrive\Documents\python works\labor_force\dataset\training.xlsx")
#bar chart creation
figTrainAgr = px.bar(training_data, x=['in agriculture', 'not in agriculture'], y='period',
             labels={'value': 'Population'},
             orientation='h')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data for the agerange agri
AgePopAgri=pd.read_excel(r"C:\Users\user\OneDrive\Documents\python works\labor_force\dataset\agerangeagri.xlsx")
#---------------------------------------------------------------------------Agriculture page layout-----------------------------------------------------------------------------------
layout = dbc.Container([
        html.Br(),
        html.Br(),
        html.H1('Main Indicators',style={'textAlign':'center','fontSize': '30px','color': 'black','fontFamily':'Roboto Slab'},className='m-3'),
        html.Br(),
        # Horizontal frame for the title for "The Labor Force" section
        html.Div(
            [
                html.H3("ccccccccccccccccccccccccccccc ", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
        dbc.Row([
            html.Div([
                dcc.Dropdown(
                    id='dropdownrat-select',
                    options=[
                        {'label': 'Labour Force Participation Rate', 'value': 'Labour force participation rate'},
                        {'label': 'Employment to Population Ratio', 'value': 'Employment-population ratio'},
                        {'label': 'Unemployment Rate', 'value': 'Unemployment rate'}
                    ],
                    value='Labour force participation rate',  # Default selected value
                    style={'width': '60%', 'textAlign': 'center'},
                    multi=False  # Do not allow multi-selection
                ),

                dcc.Graph(
                    id='line-chart'
                )
            ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
        ]),
        html.Br(),
        html.Div(
            [
                html.H3("vvvvvvvvvvvvvvvvvvvvvvvvvvvvv ", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
        dbc.Row([   
            html.Div([
                dcc.Dropdown(
                    id='dropdown-edu-level',
                    options=[{'label': level, 'value': level} for level in EduIndicator['Educational_level']],
                    value='Not any',
                    style={'width': '50%', 'marginBottom': '20px'}
                ),

                html.Div([
                    html.Div([dcc.Graph(id='guagelaf')], style={'width': '33%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='gaugeempratio')], style={'width': '33%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='gaugeunemplor')], style={'width': '33%', 'display': 'inline-block'}),
                ])
            ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'})         
            
        ]),
        html.Br(),
        html.Div(
            [
                html.H3("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ", style={'color': 'black', 'backgroundColor': '#2fc2df', 'padding': '10px'}),
            ],
            style={'textAlign': 'center'}
        ),
        dbc.Row([    
            html.Div([
                #ggbdlgbsbfvskjbjhx lfaljnvljjsnvslvs   
            ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),    
        ]),
        html.Br(),
#-------------------------------------------------------------------existing------------------------------------------------------------------------------------
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Div([
                        html.H3('Population Distribution by Training Period and Status in Agriculture/Not in Agriculture', style={'color': 'black','textAlign':'center', 'margin': '0 auto'}),
                    ],className="border-start border-primary border-5 m-4", style={'height': '40px'}),
                    html.Hr(style={'color': 'black', 'width': '90%', 'margin': '0 auto'}),
                    dcc.Graph(figure=figTrainAgr)
                ], style={'border': '1px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'})
            ],width=6)
        ]),
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