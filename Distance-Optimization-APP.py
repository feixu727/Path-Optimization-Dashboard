
# Implement Heuristic algorithm for Traveling Salesman Problem.

import random
import math
import TryAll
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

#imprort csv
bank = pd.read_csv('C:\\Users\\xufei\\Dropbox\\544\\4\\Hawaii_Banks_and_Credit_Unions.csv')

# Create list of points
numOfPoints = 7

pointsList = [(random.uniform(-10, 10), random.uniform(-10, 10)) for i in range(numOfPoints)]

bank['Location'] = bank[['X', 'Y']].apply(tuple, axis=1)

pointsList = bank[bank['island']== 'Hawaii']['Location'].to_list()

# Dashboard
app = dash.Dash(__name__)

app.layout = html.Div(
    [html.H1('Shorest Path for Hawaii Banks and Credit Unions'),
     html.P(['Banksy Aire Company',
             html.Br(),]),
    html.P([html.Label('Choose an Island'), dcc.Dropdown(
        id = 'mydropdown',
        options =[ {'label': col, 'value': col} for col in bank.island.unique()],
        value = 'Hawaii'
    )]),

    dcc.Graph(id = 'outputgraph')
    ] # Closes out the app.layout
)

@app.callback(
    Output(component_id = 'outputgraph',component_property='figure'),
    [Input(component_id='mydropdown',component_property='value')]
)

def updategraph(island):
    pointsList = bank[bank['island']== island]['Location'].to_list()
    allPaths = []
    allDists = []

    # Let every point be the starting point for a path
    for i, startPtIndex in enumerate(pointsList):

    # initialize a pt holder, path, and holder for distance
        ptsLeft = pointsList.copy()
        aPath = []
        distance = 0

    # move the first point to the path
        aPath.append(ptsLeft.pop(i))

    # find the next point to add to path.
        while len(ptsLeft)>0:
            currPt = aPath[-1]
            distToCurrPt = [TryAll.dist(currPt, pt) for pt in ptsLeft]
            minDistIndex = distToCurrPt.index(min(distToCurrPt))
            distance += distToCurrPt[minDistIndex]
            aPath.append(ptsLeft.pop(minDistIndex))

    # record the path and distance...
    allPaths.append(aPath)
    allDists.append(distance)

    # end for loop that picks a starting point.
    bestDist = min(allDists)
    bestPath = allPaths[allDists.index(bestDist)]
    print(bestPath)
    print(bestDist)
    xbestPath = [x[0] for x in bestPath]
    ybestPath = [x[1] for x in bestPath]
    fig = go.Figure( dict(
        type = 'scatter',
        mode = 'lines+markers',
        x = xbestPath,
        y = ybestPath,

        # hovertext = bank[bank[‘island’]== island|bank[‘X’]== xbestPath |bank[‘Y’]== YbestPath  ][‘Location’],
        marker=dict(
            color='rgb(333,111,0)',
            opacity=.5,
            size = 11
        )))
    return  fig

if __name__ =='__main__':
    app.run_server(debug=True, port=8054)