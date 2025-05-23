

class node:
    features = []
    accuracy = 0

    def __init__(self, features, accuracy = 0):
        self.features = features
        self.accuracy = accuracy
        

    def setAccuracy(self, accuracy):
        self.accuracy = accuracy

    def setFeatures(self, features):
        features = features

