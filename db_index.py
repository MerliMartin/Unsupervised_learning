
import numpy as np


def db_index(clusters):
    dbi_sum = 0
    for i, ic in enumerate(clusters): # clusters = [[1, 2, 3..]. [4, 5, 6]...] • First run,  i=0, ic=[1, 2, 3..]
        Dij_val = []
        for k, kc in enumerate(clusters):
            if i != k:
                Dij_val.append(Dij(ic, kc))
        dbi_sum += max(Dij_val)

    return dbi_sum


def Dij(ci, cj):
    return (
                (d_bar(ci) + d_bar(cj)) / # intra-cluster distance
                d_ij(ci, cj) # inter-cluster distance
            )


# Inter-Cluster distance (Separation)
# Distance between centroids of cluster i, j
# Our distance metric -> d(i, j) = abs(i - j)
def d_ij(ci, cj):
    mu_i = np.mean(ci)
    mu_j = np.mean(cj)
    return abs(mu_i - mu_j)

# Intra-Cluster distance (Compactness)
# Average distance between each point in a cluster
def d_bar(ci): # ci = [2.4, 3.4, 1.6 ...]
    centroid = np.mean(ci) # Compute centroid of cluster ci eg. 5
    dist = []
    for pt in ci:
        dist.append(abs(pt-centroid))  # absolute distance from centroid eg. pt=1, dist = abs(1-5) = 4

    # print("Distances from centroid (Cluster 1): ", dist)
    return np.mean(dist) # Sum of the distance / number of points in cluster


if __name__ == "__main__":
    # Initializing List of Clusters
    n_clusters = 10

    oned_cluster = [
        np.random.uniform(low=1.0, high=10.0, size=20)
        for i in range(n_clusters)
    ]

    oned_cluster