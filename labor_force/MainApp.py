import dash
from dash import html, Output, Input, State
import dash_labs as dl
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, "/assets/style.css"])

offcanvas = html.Div(
    [
        html.Div([
            dbc.Row([
                dbc.Col([dbc.Button("Explore", id="open-offcanvas", n_clicks=0, className='m-2',style={'fontSize':'20px','color':'#1d557a','border': '2px solid #2f9cdf','fontFamily':'Roboto Slab'}),],width=2),
                dbc.Col([             
                    html.Div("Labor Force Survey 2022", style={'fontSize': '40px', 'textAlign': 'left', 'padding': '10px', 'fontFamily':'Roboto Slab'}, 
                            #  className="border-start border-success border-5"
                             ), 
                ], width=5, className="mx-auto"),
            ]),
        ], style={'backgroundColor': '#2fc2df', 'padding': '10px'}, className='m-2 gradient-background'),
        dbc.Offcanvas(
            dbc.ListGroup(
                [
                    dbc.ListGroupItem(page["name"], href=page["path"], className="nav-link")
                    for page in dash.page_registry.values()
                    if page["module"] != "pages.not_found_404"
                ]
            ),
            id="offcanvas",
            is_open=False,
            className="custom-center"
        ),
    ],
    className="my-3"
)

app.layout = dbc.Container(html.Div([
    
    
    offcanvas, dash.page_container
], style={'backgroundColor': '#dae5e8'}), fluid=True)

@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open

# ---------------------------------------------------------------------------------------------------------------------------
# Run the App
if __name__ == "__main__":
    app.run(debug=True)
