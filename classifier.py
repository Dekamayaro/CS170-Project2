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
        self.trainSet = np.array()
        self.trainset = np.reshape(0, self.data.shape[1]) #making trainSet to have n columns (including class), but 0 rows 
        self.numCols = self.data.shape[1]


    def train(self, setID):
        
        for id in setID: #! I think this works, but I have no clue to be so honest
            self.trainSet = np.vstack((self.trainSet, self.data[id:]))
            
    def test(self, id):
        pass
    