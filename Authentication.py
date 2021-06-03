import pandas as pd
import plotly.express as px

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_auth
import flask
app = dash.Dash(__name__)
server = app.server

auth = dash_auth.BasicAuth(
    app,
    {'123':'123'}
)
app.layout = html.Div([
    html.H1('Welcome to the app'),
    html.H3('You are successfully authorized'),
])

if __name__ == '__main__':
    app.run_server(debug=True)