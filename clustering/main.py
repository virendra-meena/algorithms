import numpy as np
import pandas as pd

from clustering.data import load_choc_data
from clustering.kmeans import kmeans
from clustering.metrics import clusterQualityMetrics
from clustering.preprocess import preprocess

np.set_printoptions(precision=2)
pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_rows = 15


if __name__ == "__main__":
    # load data
    choc_df = load_choc_data()

    # preprocess data
    choc_df = preprocess(choc_df)

    # num of clusters
    k = 30  # @param
    feature_cols = choc_df.columns.values  # save original columns

    # initialize every point to an impossible value, the k+1 cluster
    choc_df['centroid'] = k

    # init the point to centroid distance to an impossible value "2" (>1)
    choc_df['pt2centroid'] = 2
    [choc_df, centroids] = kmeans(choc_df, k, feature_cols, 1)

    print("Data for the first few chocolates, with 'centroid' and 'pt2centroid' on"
          ' the extreme right:')

    # show
    choc_df.head()

    # compute metrics
    clusterQualityMetrics(choc_df)
