# https://plot.ly/python/bar-charts/
from flask import Flask, render_template

import json
import plotly

import pandas as pd
import numpy as np

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    rng = pd.date_range('9/1/1995', periods=7500, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)

    graphs = [
        dict(
            data=[
                dict(
                    x=[1, 2, 3, 4],
                    y=[10, 20, 30, 40],
                    type='bar'
                ),
            ],
            layout=dict(
                title='first graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=['totoro', 'gaonasi', 'ponyo', 'yoobaba'],
                    y=[70, 10, 40, 0],
                    type='scatter'
                ),
            ],
            layout=dict(
                title='second graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=ts.index,  # Can use the pandas data structures directly
                    y=ts
                )
            ],
            layout=dict(
                title='third graph'
            )
        )
    ]

    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('layouts/index.html',
                           ids=ids,
                           graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
