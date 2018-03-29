import numpy as np
import csv
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Imputer

def run(example):
    # Define LogisticRegression Model
    model = LogisticRegression()
    with open('newset.csv') as newfile:
        reader = csv.reader(newfile)
        data = list(reader)
    Xall = [l[0:3] for l in data]
    Xall = np.array(Xall).astype(np.float64)
    yall = [l[4] for l in data]
    model.fit(Xall, yall)
    print('\nClassifier score on full data set: \n' + str(model.score(Xall, yall) * 100))
    imputer = Imputer(missing_values = -1, strategy="median")
    imputer.fit(Xall, yall)
    example = imputer.transform(np.reshape(example, (1, -1)))
    prediction = model.predict(np.reshape(example, (1, -1)))
    return (prediction[0])
