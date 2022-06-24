from functools import reduce
from typing import List

import numpy as np
import pandas as pd
import seaborn as sns
from dash import dcc
from data.external import mpg_df


def model_year_range() -> dcc.RangeSlider:
    df = mpg_df()
    min_, max_ = df.model_year.min(), df.model_year.max()
    mean_, std_ = df.model_year.mean(), df.model_year.std()
    return dcc.RangeSlider(min_, max_, 1, value=[70, 82], id="model-yearrange-slider")


# def Origin


def car_origin_checklist() -> dcc.Checklist:
    checklist = dcc.Checklist(
        options=["usa", "europe", "japan"],
        value=["usa", "europe", "japan"],
        inline=True,
        id="car-origin-checklist",
    )
    return checklist
