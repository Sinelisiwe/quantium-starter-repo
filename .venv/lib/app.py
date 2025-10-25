# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from plotly.figure_factory.utils import annotation_dict_for_label

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
DATA_DIRECTORY = "/Users/sinelisiwesibeko/PycharmProjects/quantium-starter-repo/.venv/lib/processed_data.csv"
df = pd.read_csv(DATA_DIRECTORY)

fig = px.scatter(df, x="Date", y="Sales", color="Region")

fig.add_vrect(x0="2021-01-15", x1="2021-01-15", line_dash="dot", annotation_text="Pink Morsel price increase", annotation_position="top right", fillcolor="green", line_width=1)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)