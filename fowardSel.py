import node
import numpy as np
from queue import PriorityQueue


def eval(Node:node):
    pass

def forwardSel(fileName):
    data = np.loadtxt(fileName)

    #finding number of features, columns in data:
    numFeatures = data.shape[1]
    featureQueue = PriorityQueue()

    print(f"Using no features and “random” evaluation, I get an accuracy of\n")

    #find begin acc:
    beginAcc = eval(node()) #! need to include start node
    print(f"{beginAcc}% Beginning search.")

    for feat in numFeatures:
        #find accuracy of selected feature(s):
        currNode = node() #!add features to node --> still need to think of how though.

        featureAcc = None #!eval function here 
        print(f"Using feature(s) {feat} accuracy is {featureAcc}%\n")
        #!need to create a node for it and set the accuracy

    
    #need to find the best feature now:
        #!we can use a maxheap with accuracy 
         # maybe add to before we find the accuracy and then 


