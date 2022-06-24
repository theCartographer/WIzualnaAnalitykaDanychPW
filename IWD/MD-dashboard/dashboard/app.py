from functools import reduce
from typing import Any, Dict, List, Tuple

import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from dash import Dash, Input, Output, State, dash_table, dcc, html
from dash_bootstrap_components._components.Container import Container

from components.core import alert, header
from components.filtering import car_origin_checklist, model_year_range
from data.external import filter_car, filter_car_by_selection, mpg_df
from graphs.templates import graph1, graph2, graph3, graph4

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(
    children=[
        alert,
        header,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Span("Model Year Range Slider:"),
                    width=2,
                    style={"font-weight": "normal"},
                ),
                dbc.Col(dbc.Col(model_year_range())),
                dbc.Col(
                    html.Span("Car manufacturer checklist:"),
                    width=2,
                    style={"font-weight": "normal"},
                ),
                dbc.Col(
                    dbc.Col(
                        car_origin_checklist(),
                        style={"font-size": "large"},
                    )
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    html.Span("Number of cars in the filter:"),
                    width=2,
                    style={"font-weight": "normal"},
                ),
                dbc.Col(
                    html.Span(
                        children=[],
                        id="car-number-field",
                        style={
                            "font-weight": "bold",
                            "font-size": "x-large",
                            "color": "blue",
                            "border-bottom": "4px dotted blue",
                        },
                    )
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button(
                        "Preset Filters",
                        outline=True,
                        color="success",
                        className="me-1",
                        id="preset-button",
                    ),
                    width=2,
                ),
                dbc.Col(
                    dbc.Button(
                        "Reload the page",
                        outline=True,
                        color="warning",
                        className="me-1",
                        href="/",
                        external_link=True,
                    )
                ),
            ]
        ),
        # dbc.Row(dbc.Col(html.Div("This will be a dashboard about Cars!"))),
        dbc.Row(
            [
                dbc.Col(id="graph1-col", children=graph1(), width=6),
                dbc.Col(id="graph2-col", children=graph2(), width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(id="graph3-col", children=graph3(), width=6),
                dbc.Col(id="graph4-col", children=graph4(), width=6),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dash_table.DataTable(
                        data=mpg_df().to_dict("records"),
                        columns=[{"name": i, "id": i} for i in mpg_df().columns],
                        page_action="native",
                        page_current=0,
                        page_size=10,
                        id="car-table",
                    )
                ),
            ]
        ),
    ]
)


@app.callback(
    Output("graph1-col", "children"),
    Output("graph2-col", "children"),
    Output("graph3-col", "children"),
    Output("graph4-col", "children"),
    # Output("car-tables", "data"),
    Input("model-yearrange-slider", "value"),
    Input("car-origin-checklist", "value"),
    prevent_initial_call=True,
)
def adjust_textual_data(
    model_year_range: List[float], origin_checklist: List[str]
) -> Tuple[dcc.Graph, dcc.Graph, dcc.Graph, dcc.Graph]:

    return (
        graph1(model_year_range, origin_checklist),
        graph2(model_year_range, origin_checklist),
        graph3(model_year_range, origin_checklist),
        graph4(model_year_range, origin_checklist),
    )


# callback modifing count on top of the website and the datarange of the table
# also add crossfiltering from scatter plots


@app.callback(
    Output("car-number-field", "children"),
    Output("car-table", "data"),
    Input("model-yearrange-slider", "value"),
    Input("car-origin-checklist", "value"),
    Input("graph1", "selectedData"),
    Input("graph2", "selectedData"),
)
def adjust_textual_data(
    model_year_range: List[float],
    origin_checklist: List[str],
    graph1_selection,
    graph2_selection,
) -> Tuple[str, Dict[str, Any]]:
    df = mpg_df()
    df = filter_car(df, model_year_range, origin_checklist)
    df = filter_car_by_selection(df, graph1_selection, graph2_selection)
    car_count = len(df)
    car_count_text = f"{car_count}"
    return car_count_text, df.to_dict("records")


# preset button callback
@app.callback(
    Output("model-yearrange-slider", "value"),
    Output("car-origin-checklist", "value"),
    Input("preset-button", "n_clicks"),
    prevent_initial_call=True,
)
def load_preset(n_clicks):
    return [70, 82], ["europe", "japan"]


if __name__ == "__main__":
    app.run_server(
        port=8062,
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_max_retry=5,
        dev_tools_hot_reload_interval=5,
    )
