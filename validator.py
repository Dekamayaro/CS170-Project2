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


    def __init__ (self, features = [], Classifier:classifier = classifier(""), filename = ""): # type: ignore
        self.features = features
        self.classifier = Classifier
        self.data = np.loadtxt(filename)


    def validate ():
        pass
