from sklearn.cluster import KMeans
import numpy as np
import csv
from sklearn.linear_model import LogisticRegression

def test():
    results = []
    with open("soil_dataset.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader: # each row is a list
            results.append(row)

    kmeans = KMeans(n_clusters=2, random_state=0).fit(results)

    data = results
    index = 0
    for i in kmeans.labels_:
        data[index].append(i)
        index += 1

    with open("newset.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
