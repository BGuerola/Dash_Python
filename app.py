from logging import basicConfig
from typing import Sized
import dash
from dash_bootstrap_components._components.Navbar import Navbar
from dash_html_components.Div import Div
from dash_html_components.Font import Font
import pandas
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff
import plotly.graph_objects as go

external_stylesheets = [dbc.themes.COSMO]

app = dash.Dash (__name__, external_stylesheets=external_stylesheets)



df=[dict(Task="Run Devscola", Start = '2021-05-31', Finish='2021-06-03', Resource = 'JavaScript'),
dict(Task="Curs Dash", Start = '2021-06-03', Finish='2021-06-11', Resource = 'Data Science'),
dict(Task="Timetricker", Start = '2021-06-11', Finish='2021-06-18', Resource = "APIS"),
dict(Task="Run Devscola", Start = '2021-06-12', Finish='2021-06-17', Resource = 'JavaScript'),
dict(Task="Joc en Java", Start = '2021-06-18', Finish='2021-06-19', Resource = 'APIS'),
dict(Task="Joc en C++", Start = '2021-06-19', Finish='2021-06-23', Resource = 'C++')
]

colors = {"Data Science":'#66108E',
             "JavaScript":'#cf2d0c',
             "APIS":'#11854d',
             "C++": '#3633FF'}

fig = ff.create_gantt (df, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
fig.update_yaxes(autorange=True)

#fig=go.Figure()

navbar=dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("page 3", href = "#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Dash Formació",
    color='#6661e8',

    dark=True
)

body=dbc.Container([
    html.Br(),
    dbc.Row([
        dbc.Col(
            html.Div(
                html.H2("Diagrama de Gantt sobre roda de projectes/formació en programació")             
            ), width=6, align = 'center'
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.Div(
                dcc.Graph(
                    id = "Gant",
                    figure = fig
                )
            ),width=12, align= 'start'
        ), 
    ])
])


app.layout = html.Div([navbar, body])

if __name__ == "__main__":
    app.run_server(debug=True)