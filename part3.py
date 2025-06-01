from node import node
import numpy as np
from queue import PriorityQueue
import validator
import classifier
import random


def evaluate(Node:node, filename):
    if([] == Node.features):
        return round(random.uniform(35.0, 95.0), 2)
    else:
        val = validator.validator(features = Node.features, Classifier = classifier.classifier(fileName = filename, selected_feat = Node.features))
        return val.validate()

def forwardSel(filename):
    maxAcc = 0
    selectedFeat = []
    bestFeat = []

    #finding number of features, columns in data:
    numFeatures = np.loadtxt(filename).shape[1] - 1
    initialFeat = remainingFeat = list(range(1, numFeatures + 1))
    featureQueue = PriorityQueue()
    print(f"Using no features and “random” evaluation, I get an accuracy of\n")

    #find begin acc:
    beginAcc = evaluate(node(features = []), filename)
    print(f"{beginAcc}% Beginning search.")

    while remainingFeat:
        currBest = None
        featureQueue = PriorityQueue()
        for feat in remainingFeat:
            #find accuracy of selected feature(s):
            currFeatures = [feat] + selectedFeat
            currNode = node(features = currFeatures)
            currNode.setAccuracy(evaluate(currNode, filename))
            featureQueue.put(currNode)
            print(f"    Using feature(s) {currFeatures} accuracy is {currNode.accuracy}%\n")
            
        
        #need to find the best feature now:
        currBest = featureQueue.get()

        if(maxAcc >= currBest.accuracy):
            print(f"Feature set {currBest.features} was best, accuracy is {currBest.accuracy}%\n")
            selectedFeat = currBest.features
            remainingFeat = list(set(initialFeat) - set(selectedFeat))
        else:
            maxAcc = currBest.accuracy
            print(f"Feature set {currBest.features} was best, accuracy is {maxAcc}%\n")
            bestFeat = selectedFeat = currBest.features
            remainingFeat = list(set(remainingFeat) - set(selectedFeat))

    print(f"Overall, the best feature selection was: {bestFeat} with accuracy: {maxAcc}")
    
def backwardsElim(featuresInput): #! unmodified for p3 yet
    maxAcc = 0
    bestFeat = []
    selectedFeat = []

    #finding number of features, columns in data:
    numFeatures = featuresInput

    print(f"Using all features and \"random\" evaluation, I get an accuracy of\n")
    beginAcc = evaluate(node(list(range(1,numFeatures)))) #! need to include start node
    print(f"{beginAcc}% Beginning search.")

    initialFeat = selectedFeat = remainingFeat = list(range(1, numFeatures + 1))
    featureQueue = PriorityQueue()
    print(selectedFeat)
    while len(selectedFeat) > 1:
        currBest = None

        for feat in selectedFeat:
            currFeatures = [f for f in selectedFeat if f != feat]
            currNode = node(features = currFeatures)
            currNode.setAccuracy(evaluate(currNode))
            featureQueue.put(currNode)
            print(f"    Using feature(s) {currFeatures} accuracy is {currNode.accuracy}%\n")            
        
        #need to find the best feature now:
        currBest = featureQueue.get()

        if(maxAcc >= currBest.accuracy):
            print(f"Feature set {currBest.features} was best, accuracy is {currBest.accuracy}%\n")
            selectedFeat = currBest.features
            remainingFeat = list(set(initialFeat) - set(selectedFeat))
        else:
            maxAcc = currBest.accuracy
            print(f"Feature set {currBest.features} was best, accuracy is {maxAcc}%\n")
            bestFeat = selectedFeat = currBest.features
            remainingFeat = list(set(remainingFeat) - set(selectedFeat))

    print(f"Overall, the best feature selection was: {bestFeat} with accuracy: {maxAcc}")
