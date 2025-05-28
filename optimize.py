import node
import numpy as np
from queue import PriorityQueue
import random


def eval(Node:node):
    return round(random.uniform(35.0, 95.0), 2)

def forwardSel(fileName):
    data = np.loadtxt(fileName)
    isStop = False
    maxAcc = 0
    bestFeat = []
    selectedFeat = []

    #finding number of features, columns in data:
    numFeatures = data.shape[1]
    remainingFeat = list(range(1, numFeatures + 1))
    featureQueue = PriorityQueue()
    labels = data[:, 0]
    features = data[:, 1:]
    print(f"Using no features and “random” evaluation, I get an accuracy of\n")

    #find begin acc:
    beginAcc = eval(node()) #! need to include start node
    print(f"{beginAcc}% Beginning search.")

    while(False == isStop):
        currBest = None
        for feat in remainingFeat:
            #find accuracy of selected feature(s):
            #currNode = node() #!add features to node --> still need to think of how though.
            currFeatures = selectedFeat + [feat]
            currNode = node(features = currFeatures)
            currNode.setAccuracy(eval(currNode))
            featureQueue.put(currNode)
            print(f"Using feature(s) {feat} accuracy is {currNode.accuracy}%\n")
            
        
        #need to find the best feature now:
        currBest = featureQueue.get()

        # if((maxAcc >= currBest.accuracy) & ([] == remainingFeat)):
        #     isStop = True
        #     print(f"(Warning: Decreased accuracy! )\n Search fininshed! The best subset of features is {selectedFeat}, which has an accuracy of {maxAcc}%")
        #     break
        if([] == remainingFeat):
            isStop = False
            break
        elif(maxAcc >= currBest.accuracy):
            print(f"Feature set {currBest.features} was best, accuracy is {maxAcc}%\n")
            selectedFeat = currBest.features
        elif(maxAcc < currBest.accuracy):
            maxAcc = currBest.accuracy
            print(f"Feature set {currBest.features} was best, accuracy is {maxAcc}%\n")
            bestFeat = selectedFeat = currBest.features

        tempRemainingFeat = []
        for i in selectedFeat:
            if i != feat:
                tempRemainingFeat.append(i)
        remainingFeat = tempRemainingFeat
            #! not foolproof, will add repeat nums 
            #! also need to update numfeatures --> remove the feature chosen last 

    print(f"Overall, Feature srt {bestFeat} was best, accuracy is {maxAcc}")
    return maxAcc
        
def backwardsElim(fileName):
    data = np.loadtxt(fileName)
    isStop = False
    maxAcc = 0
    selectedFeat = []

    #finding number of features, columns in data:
    numFeatures = data.shape[1] - 1

    print(f"Using all features and \"random\" evaluation, I get an accuracy of\n")
    beginAcc = eval(node(list(range(1,numFeatures)))) #! need to include start node
    print(f"{beginAcc}% Beginning search.")

    selectedFeat = remainingFeat = list(range(1, numFeatures + 1))
    featureQueue = PriorityQueue()

    while(False == isStop):
        currBest = None

        for feat in remainingFeat:
            currFeatures = selectedFeat - [feat]
            currNode = node(features = currFeatures)
            currNode.setAccuracy(eval(currNode))
            featureQueue.put(currNode)
            print(f"Using feature(s) {feat} accuracy is {currNode.accuracy}%\n")            
        
        #need to find the best feature now:
        currBest = featureQueue.get()

        if(maxAcc >= currBest.accuracy):
            isStop = True
            print(f"(Warning: Decreased accuracy! )\n Search fininshed! The best subset of features is {selectedFeat}, which has an accuracy of {maxAcc}%")
            break
        else:
            maxAcc = currBest.accuracy
            print(f"Feature set {currBest.features} was best, accuracy is {maxAcc}%\n")
            remainingFeat = selectedFeat = currBest.features
            #tempRemainingFeat = []

            # for i in selectedFeat:
            #     if i != feat:
            #         tempRemainingFeat.append(i)
            # remainingFeat = tempRemainingFeat
            #! not foolproof, will add repeat nums 
            #! also need to update numfeatures --> remove the feature chosen last 


