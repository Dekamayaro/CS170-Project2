

class node:
    features = []
    accuracy = 0

    def __init__(self, features = [], accuracy = 0):
        self.features = features
        self.accuracy = accuracy
        

    def setAccuracy(self, accuracy):
        self.accuracy = accuracy

    def setFeatures(self, features):
        self.features = features

    #the following are needed for doing comparisons between nodes and for adding them into the queue
    def __eq__(self, other): #one for equal
        return (self.accuracy == other.accuracy)
    
    def __ne__(self, other): #one for non-equal
        return (self.accuracy != other.accuracy)

    def __lt__(self, other): #one for less than
        return (self.accuracy > other.accuracy)

    def __gt__(self, other): #one for greater than
        return (self.accuracy < other.accuracy)

    #def __ne__(self, other): #another one for non-equal
    #    return (self.parent != None)

