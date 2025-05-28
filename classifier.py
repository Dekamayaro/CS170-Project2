#imports:
import numpy as np
from math import dist #https://stackoverflow.com/questions/9414722/multidimensional-euclidean-distance-in-python

class classifier:
    #variables
    trainSet = None
    data = None
    numCols = None


    #functions:
    def __init__(self, fileName):
        self.data = np.loadtxt(fileName)
        self.trainSet = np.empty((0, self.data.shape[1])) #making trainSet to have n columns (including class), but 0 rows 
        self.numCols = self.data.shape[1]


    def train(self, setID):
        
        for id in setID: #! I think this works, but I have no clue to be so honest
            self.trainSet = np.vstack((self.trainSet, self.data[id].reshape(1, -1)))
            
    def test(self, id):
        test_instance = self.data[id, 1:] #only the feature values from data
        best_dist = float('inf')
        best_label = None
        
        for row in self.trainSet:
            train_features = row[1:]
            train_label = row[0]
            euclid_dist = np.linalg.norm(test_instance - train_features)
            
            if euclid_dist < best_dist:
                best_dist = euclid_dist
                best_label = train_label
        
        return best_label
    