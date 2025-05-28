#imports:
import numpy as np
from math import dist #https://stackoverflow.com/questions/9414722/multidimensional-euclidean-distance-in-python
from sklearn.preprocessing import MinMaxScaler

class classifier:
    #variables
    trainSet = None
    data = None
    numCols = None


    #functions:
    def __init__(self, fileName, selected_feat):
        self.data = np.loadtxt(fileName)
        self.trainSet = np.empty((0, self.data.shape[1])) #making trainSet to have n columns (including class), but 0 rows 
        self.numCols = self.data.shape[1]

        labels = self.data[:, [0]]
        features = self.data[:, 1:]
        
        scalar = MinMaxScaler()
        normalized_feat = scalar.fit_transform(features)
        
        self.data = np.hstack((labels, normalized_feat))
        
        if selected_feat is not None:
            self.selected_feat = selected_feat
        else:
            self.selected_feat = list(range(1, self.numCols))

    def train(self, setID):
        
        for id in setID: #! I think this works, but I have no clue to be so honest
            self.trainSet = np.vstack((self.trainSet, self.data[id]))
            
    def test(self, id):
        #test_instance = self.data[id, 1:] #only the feature values from data
        # `test_instance` is extracting the selected features from the test data instance based on the
        # `selected_feat` attribute. It selects only the specific features that are chosen for testing
        # from the data instance.
        test_instance = self.data[id, self.selected_feat]
        best_dist = float('inf')
        best_label = None
        
        for row in self.trainSet:
            #train_features = row[1:]
            train_features = row[self.selected_feat]
            train_label = row[0]
            euclid_dist = np.linalg.norm(test_instance - train_features)
            
            if euclid_dist < best_dist:
                best_dist = euclid_dist
                best_label = train_label
        
        return best_label
    