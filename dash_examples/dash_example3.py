# -*- coding: utf-8 -*-
# tutorial link: https://www.youtube.com/watch?v=gRW4vRKKC1c
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Introdução ao Dash'),

    dcc.Graph(id='grafico-1',
            figure={
                'data': [{'x': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'], 'y': [20,12,14,17,10], 'type': 'line', 'name': '2019'},
                        {'x': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'], 'y': [18,8,12,14,6], 'type': 'bar', 'name': '2020'}, ],
                'layout': {
                    'title': 'Consumo médio de Energia: Consumidor 1',
                    'xaxis': dict(
                        title='Meses',
                        titlefont=dict(
                        family='Helvetica, monospace',
                        size=20,
                        color='black'
                    )),
                    'yaxis': dict(
                        title='Energia [Mwh]',
                        titlefont=dict(
                            family='Helvetica, monospace',
                            size=20,
                            color='black'
                        ))
                    }
            }),

    dcc.Graph(id='grafico-2',
            figure={
                'data': [{'x': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'], 'y': [20,12,14,17,10], 'type': 'line', 'name': '2019'},
                        {'x': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'], 'y': [18,8,12,14,6], 'type': 'bar', 'name': '2020'}, ],
                'layout': {
                    'title': 'Consumo médio de Energia: Consumidor 2',
                    'xaxis': dict(
                        title='Meses',
                        titlefont=dict(
                        family='Helvetica, monospace',
                        size=20,
                        color='black'
                    )),
                    'yaxis': dict(
                        title='Energia [Mwh]',
                        titlefont=dict(
                            family='Helvetica, monospace',
                            size=20,
                            color='black'
                        ))
                    }
            })    
])

if __name__ == '__main__':
    app.run_server(debug=True)