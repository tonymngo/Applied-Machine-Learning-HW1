from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

boston = datasets.load_boston()

def scatter_data(dataset,i):
    points = []
    for line in dataset['data']:
        points.append(line[i])
    return points

fig = plt.figure(figsize=(20,40))
for i in range(13):
    plt.subplot(13,2,i+1)
    plt.scatter(scatter_data(boston,i),boston['target'], alpha=0.5)
    plt.xlabel(boston['feature_names'][i])
    plt.ylabel('MEDV')

plt.subplots_adjust(hspace=0.4)
   
print (boston['feature_names'])
plt.savefig('task33.png')         
plt.show()