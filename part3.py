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
    print(f"{beginAcc:.1f}% Beginning search.")

    while remainingFeat:
        currBest = None
        featureQueue = PriorityQueue()
        for feat in remainingFeat:
            #find accuracy of selected feature(s):
            currFeatures = [feat] + selectedFeat
            currNode = node(features = currFeatures)
            currNode.setAccuracy(evaluate(currNode, filename))
            featureQueue.put(currNode)
            print(f"    Using feature(s) {currFeatures} accuracy is {100 * currNode.accuracy:.1f}%\n")
            
        
        #need to find the best feature now:
        currBest = featureQueue.get()

        if(maxAcc >= currBest.accuracy):
            print(f"Feature set {currBest.features} was best, accuracy is {100 * currBest.accuracy:.1f}%\n")
            selectedFeat = currBest.features
            remainingFeat = list(set(initialFeat) - set(selectedFeat))
        else:
            maxAcc = currBest.accuracy
            print(f"Feature set {currBest.features} was best, accuracy is {100 * maxAcc:.1f}%\n")
            bestFeat = selectedFeat = currBest.features
            remainingFeat = list(set(remainingFeat) - set(selectedFeat))

    print(f"Overall, the best feature selection was: {bestFeat} with accuracy: {100 * maxAcc:.1f}")
    
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
    print(f"{beginAcc:.1f}% Beginning search.")

    while len(selectedFeat) > 1:
        currBest = None
        featureQueue = PriorityQueue()
        for feat in selectedFeat:
            currFeatures = [f for f in selectedFeat if f != feat]
            currNode = node(features = currFeatures)
            currNode.setAccuracy(evaluate(currNode, fileName))
            featureQueue.put(currNode)
            print(f"    Using feature(s) {currFeatures} accuracy is {100 * currNode.accuracy:.1f}%\n")            
        
        #need to find the best feature now:
        currBest = featureQueue.get()

        if(maxAcc > currBest.accuracy):
            print(f"Feature set {currBest.features} was best, accuracy is {100 * currBest.accuracy:.1f}%\n")
            selectedFeat = currBest.features
        else:
            maxAcc = currBest.accuracy
            bestFeat = currBest.features
            print(f"Feature set {currBest.features} was best, accuracy is {100 * maxAcc:.1f}%\n")
            remainingFeat = selectedFeat = currBest.features
            
    print(f"Overall, the best feature selection was: {bestFeat} with accuracy: {100 * maxAcc:.1f}")
