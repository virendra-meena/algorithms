import math
import sys

import numpy as np
import pandas as pd


def add_lat_long(choc_df):
    # Load lat long data

    countries_info = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/countries_lat_long.csv", sep=",",
                                 encoding='latin-1')

    # Join the chocolate review and geographic information tables on maker country name
    choc_df = pd.merge(
        choc_df, countries_info, left_on="maker_location", right_on="name")
    choc_df.rename(
        columns={
            "longitude": "maker_long",
            "latitude": "maker_lat"
        }, inplace=True)
    choc_df.drop(
        columns=["name", "country"], inplace=True)  # don't need this data

    # Join the chocolate review and geographic information tables on origin country name
    choc_df = pd.merge(
        choc_df, countries_info, left_on="broad_origin", right_on="name")
    choc_df.rename(
        columns={
            "longitude": "origin_long",
            "latitude": "origin_lat"
        },
        inplace=True)
    choc_df.drop(
        columns=["name", "country"], inplace=True)  # don't need this data

    return choc_df


def getSimilarity(obj1, obj2):
    len1 = len(obj1.index)
    len2 = len(obj2.index)
    if not (len1 == len2):
        print("Error: Compared objects must have same number of features.")
        sys.exit()
        return 0
    else:
        similarity = obj1 - obj2
        similarity = np.sum((similarity ** 2.0) / 10.0)
        similarity = 1 - math.sqrt(similarity)
        return similarity


def min_max_scalar(df: pd.Series) -> pd.Series:
    np_max = np.max(df)
    np_min = np.min(df)
    df = (df - np_min) // (np_max - np_min)
    return df


def create_quantiles(df: pd.DataFrame, num_quantiles: int) -> pd.DataFrame:
    df = pd.qcut(x=df, q=num_quantiles, labels=False, duplicates='drop')
    return df
