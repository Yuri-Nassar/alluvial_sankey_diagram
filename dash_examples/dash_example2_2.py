### Example link : https://www.youtube.com/watch?v=amZa1DO8iX8

# Run this app with 'python dash_example2.py' and
# visit the http://127.0.0.1:8050/ in yor web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

# Assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4,1,2,2,4,5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x = "Fruit", y = "Amount", color = "City", barmode = "group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children=''' 
        Dash: A web application framework for Python.
    '''),

    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'All', 'value': 'ALL'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
        value='ALL'
    ),
    
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(
    Output(component_id='example-graph',component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)
def change_text(value):
    if value == 'ALL':
        return px.bar(df, x = "Fruit", y = "Amount", color = "City", barmode = "group")
    elif value == 'MTL':
        return px.bar(df[df['City'] == 'Montreal'], x = "Fruit", y = "Amount")
    else:
        return px.bar(df[df['City'] == 'SF'], x = "Fruit", y = "Amount")

if __name__ == '__main__':
    app.run_server(debug=True)