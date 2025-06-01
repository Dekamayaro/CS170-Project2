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
    
def backwardsElim(fileName):
    featureData = np.loadtxt(fileName)
    isStop = False
    maxAcc = 0
    
    #finding number of features, columns in data:
    numFeatures = featureData.shape[1] - 1
    selectedFeat = list(range(1, numFeatures + 1))

    #finding number of features, columns in data:

    print(f"Using all features and \"random\" evaluation, I get an accuracy of\n")
    beginAcc = evaluate(node(features = list(range(1,numFeatures + 1))), fileName) #! need to include start node
    print(f"{beginAcc}% Beginning search.")

    while len(selectedFeat) > 1:
        currBest = None
        featureQueue = PriorityQueue()
        for feat in selectedFeat:
            currFeatures = [f for f in selectedFeat if f != feat]
            currNode = node(features = currFeatures)
            currNode.setAccuracy(evaluate(currNode, fileName))
            featureQueue.put(currNode)
            print(f"    Using feature(s) {feat} accuracy is {currNode.accuracy}%\n")            
        
        #need to find the best feature now:
        currBest = featureQueue.get()

        if(maxAcc >= currBest.accuracy):
            print(f"Feature set {currBest.features} was best, accuracy is {maxAcc}%\n")
            selectedFeat = currBest.features
        else:
            maxAcc = currBest.accuracy
            print(f"Feature set {currBest.features} was best, accuracy is {maxAcc}%\n")
            remainingFeat = selectedFeat = currBest.features
