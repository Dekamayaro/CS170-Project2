from node import node
import numpy as np
from queue import PriorityQueue
import random


def evaluate(Node:node):
    return round(random.uniform(35.0, 95.0), 2)

def forwardSel(featuresInput):
    maxAcc = 0
    selectedFeat = []
    bestFeat = []

    #finding number of features, columns in data:
    numFeatures = featuresInput
    initialFeat = remainingFeat = list(range(1, numFeatures + 1))
    featureQueue = PriorityQueue()
    print(f"Using no features and “random” evaluation, I get an accuracy of\n")

    #find begin acc:
    beginAcc = evaluate(node(features = [])) #! need to include start node
    print(f"{beginAcc}% Beginning search.")

    while remainingFeat:
        currBest = None
        for feat in remainingFeat:
            #find accuracy of selected feature(s):
            #currNode = node() #!add features to node --> still need to think of how though.
            currFeatures = [feat] + selectedFeat
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
            #! not foolproof, will add repeat nums 
            #! also need to update numfeatures --> remove the feature chosen last 

    print(f"Overall, the best feature selection was: {bestFeat} with accuracy: {maxAcc}")
        
def backwardsElim(featuresInput):
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
