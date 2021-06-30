import sys

import numpy as np
import numpy.linalg as nla
import pandas as pd


def dfSimilarity(df, centroids):
    ### dfSimilarity = Calculate similarities for dataframe input
    ### We need to calculate ||a-b||^2 = |a|^2 + |b|^2 - 2*|a|*|b|
    ### Implement this with matrix operations
    ### See the Appendix for further explanation
    numPoints = len(df.index)
    numCentroids = len(centroids.index)
    ## Strictly speaking, we don't need to calculate the norm of points
    # because it adds a constant bias to distances
    # But calculating it so that the similarity doesn't go negative
    # And that we expect similarities in [0,1] which aids debugging
    pointNorms = np.square(nla.norm(df, axis=1))
    pointNorms = np.reshape(pointNorms, [numPoints, 1])

    ## Calculate the norm of centroids
    centroidNorms = np.square(nla.norm(centroids, axis=1))
    centroidNorms = np.reshape(centroidNorms, [1, numCentroids])
    ## Calculate |a|^2 + |b|^2 - 2*|a|*|b|
    similarities = pointNorms + centroidNorms - 2.0 * np.dot(
        df, np.transpose(centroids))
    # Divide by the number of features
    # Which is 10 because the one-hot encoding means the "Maker" and "Bean" are
    # weighted twice
    similarities = similarities / 10.0
    # numerical artifacts lead to negligible but negative values that go to NaN on the root
    similarities = similarities.clip(min=0.0)
    # Square root since it's ||a-b||^2
    similarities = np.sqrt(similarities)
    return similarities


def pt2centroid(df, centroids, feature_cols):
    ### Calculate similarities between all points and centroids
    ### And assign points to the closest centroid + save that distance
    numCentroids = len(centroids.index)
    numExamples = len(df.index)
    # dfSimilarity = Calculate similarities for dataframe input
    dist = dfSimilarity(df.loc[:, feature_cols], centroids.loc[:, feature_cols])
    df.loc[:, 'centroid'] = np.argmin(dist, axis=1)  # closest centroid
    df.loc[:, 'pt2centroid'] = np.min(dist, axis=1)  # minimum distance
    return df


def recompute_centroids(df, centroids, feature_cols):
    ### For every centroid, recompute it as an average of the points
    ### assigned to it
    numCentroids = len(centroids.index)
    for cen in range(numCentroids):
        dfSubset = df.loc[df['centroid'] == cen,
                          feature_cols]  # all points for centroid
        if not (dfSubset.empty):  # if there are points assigned to the centroid
            clusterAvg = np.sum(dfSubset) / len(dfSubset.index)
            centroids.loc[cen] = clusterAvg
    return centroids


def init_centroid(df, k, feature_cols):
    limit = len(df.index)

    centroids_key = np.random.randint(0, limit-1, k)
    centroids = df.loc[centroids_key, feature_cols].copy(deep=True)

    centroids.reset_index(drop=True, inplace=True)
    return centroids


def kmeans(df, k, feature_cols, verbose):
    flag_convergence = False
    maxIter = 100
    iterations = 0  # ensure kmeans doesn't run forever
    centroids = init_centroid(df, k, feature_cols)
    while not flag_convergence:
        iterations += 1

        # Save old mapping of points to centroids
        old_mapping = df['centroid'].copy(deep=True)

        # Perform k-means
        df = pt2centroid(df, centroids, feature_cols)
        centroids = recompute_centroids(df, centroids, feature_cols)
        # Check convergence by comparing [oldMapping, newMapping]
        new_mapping = df['centroid']

        flag_convergence = all(old_mapping == new_mapping)
        if verbose == 1:
            print('Total distance:' + str(np.sum(df['pt2centroid'])))
        if iterations > maxIter:
            print('k-means did not converge! Reached maximum iteration limit of ' \
                  + str(maxIter) + '.')
            sys.exit()
            return

    print('k-means converged for ' + str(k) + ' clusters' + \
          ' after ' + str(iterations) + ' iterations!')
    return [df, centroids]








