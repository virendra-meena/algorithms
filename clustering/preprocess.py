import numpy as np
import pandas as pd

from clustering.utils import add_lat_long, create_quantiles, min_max_scalar


def preprocess(choc_df: pd.DataFrame) -> pd.DataFrame:
    # Save the original column names
    original_cols = choc_df.columns.values

    # its a Gaussian! So, use z-score to normalize the data
    choc_df['rating_norm'] = (choc_df['rating'] - choc_df['rating'].mean()
                              ) / choc_df['rating'].std()

    choc_df['cocoa_percent_norm'] = (choc_df['cocoa_percent'] - choc_df['cocoa_percent'].mean()
                                     ) / choc_df['cocoa_percent'].std()

    # generate lat long columns
    choc_df = add_lat_long(choc_df)

    num_quantiles = 20
    cols_quantiles = ['maker_lat', 'maker_long', 'origin_lat', 'origin_long']
    for col in cols_quantiles:
        choc_df[col] = create_quantiles(choc_df[col], num_quantiles)
        choc_df[col] = min_max_scalar(choc_df[col])

    # duplicate the "maker" feature since it's removed by one-hot encoding function
    choc_df['maker2'] = choc_df['maker']
    choc_df = pd.get_dummies(choc_df, columns=['maker2'], prefix=['maker'])
    # similarly, duplicate the "bean_type" feature
    choc_df['bean_type2'] = choc_df['bean_type']
    choc_df = pd.get_dummies(choc_df, columns=['bean_type2'], prefix=['bean'])

    # Split dataframe into two frames: Original data and data for clustering
    choc_data_backup = choc_df.loc[:, original_cols].copy(deep=True)
    choc_df.drop(columns=original_cols, inplace=True)

    # get_dummies returned ints for one-hot encoding but we want floats so divide by
    # 1.0
    # Note: In the latest version of "get_dummies", you can set "dtype" to float
    choc_df = choc_df / 1.0

    print("choc df columns", choc_df.columns)
    return choc_df
