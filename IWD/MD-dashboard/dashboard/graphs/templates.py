from typing import List

import plotly.express as px
from dash import dcc
from data.external import mpg_df


def graph1(model_year_range: List[float] = None, origin_checklist: List[str] = None):
    _df = mpg_df()
    if model_year_range is not None:
        _df = _df.loc[_df.model_year.between(*model_year_range)]
    if origin_checklist is not None:
        _df = _df.loc[_df.origin.isin(origin_checklist)]

    return (
        dcc.Graph(
            id="graph1",
            figure=px.scatter(
                _df,
                x="horsepower",
                y="mpg",
                color="origin",
                hover_data=[
                    "cylinders",
                    "acceleration",
                    "weight",
                ],
                title="Scatter: Hoursepower VS Mpg",
                # width=800,
                # height=450,
            ),
        ),
    )


def graph2(model_year_range: List[float] = None, origin_checklist: List[str] = None):
    _df = mpg_df()
    if model_year_range is not None:
        _df = _df.loc[_df.model_year.between(*model_year_range)]
    if origin_checklist is not None:
        _df = _df.loc[_df.origin.isin(origin_checklist)]

    return (
        dcc.Graph(
            id="graph2",
            figure=px.scatter(
                _df,
                x="horsepower",
                y="cylinders",
                color="origin",
                hover_data=[
                    "cylinders",
                    "acceleration",
                    "weight",
                ],
                title="Scatter: horsepower VS cylinders",
                # width=800,
                # height=450,
            ),
        ),
    )


def graph3(model_year_range: List[float] = None, origin_checklist: List[str] = None):
    _df = mpg_df()
    if model_year_range is not None:
        _df = _df.loc[_df.model_year.between(*model_year_range)]
    if origin_checklist is not None:
        _df = _df.loc[_df.origin.isin(origin_checklist)]
    return dcc.Graph(
        id="graph3",
        figure=px.histogram(
            _df,
            x="mpg",
            y="horsepower",
            color="cylinders",
            marginal="box",
            hover_data=[
                "mpg",
                "cylinders",
                "displacement",
                "horsepower",
                "weight",
                "acceleration",
                "model_year",
                "origin",
                "name",
            ],
            opacity=0.5,
            histfunc="avg",
            title="histogram: MPG VS Cylinders, color: Cylinders",
            # width=800,
            # height=450,
        ),
    )


def graph4(model_year_range: List[float] = None, origin_checklist: List[str] = None):
    _df = mpg_df()
    if model_year_range is not None:
        _df = _df.loc[_df.model_year.between(*model_year_range)]
    if origin_checklist is not None:
        _df = _df.loc[_df.origin.isin(origin_checklist)]
    return dcc.Graph(
        id="graph4",
        figure=px.bar(
            _df.groupby("origin")["cylinders"].mean().reset_index(),
            x="origin",
            y="cylinders",
            title="Bar: Origin VS Cylinders",
            color="origin",
            # width=800,
            # height=450,
        ),
    )
