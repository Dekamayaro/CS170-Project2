#imports:
import numpy as np
from math import dist #https://stackoverflow.com/questions/9414722/multidimensional-euclidean-distance-in-python
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import euclidean
from heapq import heapify, heappush, heappop
from collections import Counter


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
            self.selected_feat = 0#list(range(1, self.numCols))

    def train(self, setID):
        
        for id in setID: #! I think this works, but I have no clue to be so honest
            self.trainSet = np.vstack((self.trainSet, self.data[id]))
            
    def test(self, id, k):
        test_instance = self.data[id, self.selected_feat]
        best_dist = float('inf')
        best_label = None
        listK = []

        heap = []
        heapify(heap)
        
        for row in self.trainSet:
            train_features = row[self.selected_feat]
            train_label = row[0]
            # euclid_dist = np.linalg.norm(test_instance - train_features)
            euclid_dist = euclidean(test_instance, train_features)
            
            if euclid_dist <= best_dist:
                best_dist = euclid_dist
                best_label = train_label

            heappush(heap, (euclid_dist, train_label))

        for i in range(k):
                dist, currBest = heappop(heap)
                listK.append(currBest)

        best_label = Counter(listK).most_common(1)

        # if(1 != k):
        #     for i in range(k):
        #         dist, currBest = heappop(heap)
        #         listK.append(currBest)
            
        #     listK.sort()

        #     best_label = listK[0]
        #     best_count = 0
        #     count = 0
        #     for i in range(k):
        #         if(best_label == listK[i]):
        #             count += 1
        #         elif(best_label != listK[i]):
        #             if(count > best_count):
        #                 best_count = count
        #                 best_label = listK[i]
        #             else:
        #                 count = 1

        #now, listK has the best k
        return best_label
    