# Traveling Salesperson Problem
# 3/22/2021

import pandas as pd
import random
import math
import itertools

#def dist
def dist(x, y):
    import numpy as np
    return np.sqrt(sum([pow(x[i]-y[i], 2) for i in range(len(x))]))

# Create Points...
def createPoints(num = 5):
    """ returns a dataframe with num rows and columns x, y"""
    thisData = [ [random.uniform(-10, 10), random.uniform(-10, 10)] for i in range(num)]
    return pd.DataFrame(data = thisData, columns = ['x', 'y'])


# Distance matrix ..
def distMatrix(points):
    """ returns the distance between the 'points' in points (x, y columns... seriously, dont mess it up.)"""
    return pd.DataFrame([[i, math.dist(list(points.iloc[i[0], :]), list(points.iloc[i[1], :]))] for i in itertools.permutations(points.index,2)], columns = [ 'indextuple', 'distance'])

    

# function to calculate distance along a path
def pathDist(pointIndeces, distanceDF):
    """pointsIndeces should be a tuple of indeces corresponding to the indeces of the points used to create the distanceDF... using distMatrix"""
    pointPairs = [(pointIndeces[i], pointIndeces[i+1]) for i in range(len(pointIndeces)-1)]
    return distanceDF.distance[distanceDF.indextuple.isin(pointPairs)].sum()
    
    

# function to find absolute best path.
 # Create all possible paths
 # Distance for all of them...
 # Pick the best one. (min distance)
def absBestPath(points):
    """You really should document all your functions..."""
    savedDistances = distMatrix(points)
    pathAndDist = pd.DataFrame(data = [[points.loc[aPathind,:], pathDist(aPathind, savedDistances)] for aPathind in itertools.permutations(points.index)] , columns = ["path", "distance"])
    minDistIndex = pathAndDist.distance.argmin()
    return pathAndDist.loc[minDistIndex,:]

if __name__ == '__main__':
    absBestPath(createPoints(6))
                 


