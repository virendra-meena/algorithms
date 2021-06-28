import numpy as np
from matplotlib import pyplot as plt


def clusterCardinality(df):
    k = np.max(df['centroid']) + 1
    # k = k.astype(int)
    print('Number of clusters:' + str(k))
    clCard = np.zeros(k)
    for kk in range(k):
        clCard[kk] = np.sum(df['centroid'] == kk)
    clCard = clCard.astype(int)
    # print "Cluster Cardinality:"+str(clCard)
    plt.figure()
    plt.bar(range(k), clCard)
    plt.title('Cluster Cardinality')
    plt.xlabel('Cluster Number: ' + str(0) + ' to ' + str(k - 1))
    plt.ylabel('Points in Cluster')
    return clCard


def clusterMagnitude(df):
    k = np.max(df['centroid']) + 1
    # k = k.astype(int)
    cl = np.zeros(k)
    clMag = np.zeros(k)
    for kk in range(k):
        idx = np.where(df['centroid'] == kk)
        idx = idx[0]
        clMag[kk] = np.sum(df.loc[idx, 'pt2centroid'])
    # print "Cluster Magnitude:",clMag #precision set using np pref
    plt.figure()
    plt.bar(range(k), clMag)
    plt.title('Cluster Magnitude')
    plt.xlabel('Cluster Number: ' + str(0) + ' to ' + str(k - 1))
    plt.ylabel('Total Point-to-Centroid Distance')
    return clMag


def plotCardVsMag(clCard, clMag):
    plt.figure()
    plt.scatter(clCard, clMag)
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.title('Magnitude vs Cardinality')
    plt.ylabel('Magnitude')
    plt.xlabel('Cardinality')


def clusterQualityMetrics(df):
    clCard = clusterCardinality(df)
    clMag = clusterMagnitude(df)
    plotCardVsMag(clCard, clMag)
