import numpy as np
import classifier
import node 
import optimize


class validator:
    #variables
    accuracy  = 0
    data = None
    classifier = None
    features = None
    k = None


    # def __init__ (self, features = [], Classifier:classifier = None, filename = ""): # type: ignore
    #     self.features = features
    #     self.classifier = Classifier
    #     self.data = np.loadtxt(filename)

    def __init__ (self, features = [], Classifier:classifier = None, k = 1): # type: ignore
        self.features = features
        self.classifier = Classifier
        if(0 == len(Classifier.trainSet)):
            self.data = Classifier.data
        else:
            self.data = Classifier.trainSet

        self.k = k


    def validate (self):
        correct = 0
        total = 0
        for row in range(self.data.shape[0]): # iterate through the rows
            total += 1
            #build test classifier:
            self.classifier.trainSet = np.empty((0, self.data.shape[1]))
                
            trainIds = list(range(0,self.data.shape[0]))
            trainIds.remove(row) # make sure that our training Ids are all except for the one we want to exclude 

            #training classifier to only be trained on those instances we want
            self.classifier.train(trainIds)

            testPred = self.classifier.test(row, self.k)
            
            if(testPred[0][0] == self.data[row][0]):
                correct += 1
        
        return (correct / total)


