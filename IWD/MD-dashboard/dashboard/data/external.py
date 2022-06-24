from functools import reduce
from typing import List

import numpy as np
import pandas as pd
import seaborn as sns


def mpg_df() -> pd.DataFrame:
    return sns.load_dataset("mpg")


def filter_car(
    df: pd.DataFrame,
    model_year_range: List[float] = None,
    origin_checklist: List[str] = None,
) -> pd.DataFrame:
    if model_year_range is not None:
        df = df.loc[df.model_year.between(*model_year_range)]

    if origin_checklist is not None:
        # sexes_list_remapped = [_SEXES_REMAPPING[sex] for sex in sexes_list]
        df = df.loc[df.origin.isin(origin_checklist)]

    return df


def filter_car_by_selection(df, graph1_selection, graph2_selection):
    selections = []
    intersected_selection = None

    # extract selected points from each selection if possible and add as new list to selections
    for selection in [graph1_selection, graph2_selection]:
        if selection is not None:
            selected_points = [point["pointIndex"] for point in selection["points"]]
            selections.append(selected_points)

    # if only one selection was performed, use it without modification
    if len(selections) == 1:
        intersected_selection = selections[0]

    # if more than, get the intersection of those values
    elif len(selections) > 1:
        intersected_selection = reduce(np.intersect1d, selections).tolist()

    if intersected_selection is not None:
        df = df.loc[df.index.isin(intersected_selection)]
    return df
