from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

iris = datasets.load_iris()

def hist_data(dataset,i):
    points = []
    for line in dataset['data']:
        points.append(line[i])
    return points

def scatter_data(dataset,i,j):
    xpoints = []
    ypoints = []
    for line in dataset['data']:
        xpoints.append(line[i])
        ypoints.append(line[j])
    return xpoints, ypoints

colors = {0:'b', 1:'r', 2:'g'}

fig, axes = plt.subplots(4, 4, figsize = (15,15))
for i in range(4):
    for j in range(4):
        if j ==0:
            axes[i, j].set(ylabel = iris['feature_names'][i])
        if i ==3:
            axes[i, j].set(xlabel= iris['feature_names'][j])
        if i == j:
            dp = hist_data(iris,i)
            axes[i, j].hist(dp, bins=20, color='k')
        else:
            x,y = scatter_data(iris,j,i)
            axes[i, j].scatter(x,y, c=[colors[x] for x in iris['target']])
            axes[i, j].set_ylim(min(y),max(y))
        plt.subplots_adjust(wspace=0.3, hspace=0.3)

blue_patch = mpatches.Patch(color='b', label='Setosa')
red_patch = mpatches.Patch(color='r', label='Versicolor')
green_patch = mpatches.Patch(color='g', label='Virginica')
plt.legend(handles=[blue_patch,red_patch,green_patch],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        
plt.savefig('task32.png')        
plt.show()