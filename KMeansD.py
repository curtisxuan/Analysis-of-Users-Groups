import numpy as np
import pandas as pd
import codecs
from numpy.linalg import norm

from sklearn.cluster import KMeans

#read user vector text file
count=0
usersVec = "./userVecD.txt"
users = []
with codecs.open(usersVec, 'r', 'utf8') as f:
    for line in f:
        if count%100000==0:
            print(count)
        user = line.rstrip().split(' ')
        users.append(user)
        count+=1
print(len(users))

X = np.array (users,dtype='float32')
X = X[:,1:]
print(len(X))
print(len(X[0]))

#normalize data, Y is normalized X
L2norm = norm(X, axis=1, ord=2)
Y=X / L2norm.reshape(13835534,1)

#Running K-Means-Cluster
kmeans = KMeans(n_clusters=50)
# kmeans.fit(X)
kmeans.fit(Y) #normalized

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

#write centroids and labels
out_file = "./centroidsD.txt"
count=1
with codecs.open(out_file, 'w', 'utf-8') as fw:
    for i in centroids:
        fw.write(str(count) + " ")
        for j in i:
            fw.write(str(j) + " ")
        fw.write("\n")
        count+=1
# out_file = "/Users/curtisxuan/Desktop/Work/KNN_Users/labels.txt"
out_file = "./labelsD.txt"
with codecs.open(out_file, 'w', 'utf-8') as fw:
    for i in labels:
        fw.write(str(i) + " ")
