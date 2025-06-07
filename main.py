import node
from validator import validator
from classifier import classifier 
import part1
import part3
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def plot_feature_scatter(filename, xAxis_feature, yAxis_feature, plotTitle, k):
    data = np.loadtxt(filename)
    labels = data[:, 0]
    features = data[:, 1:]

    # Normalize
    scaler = MinMaxScaler()
    features = scaler.fit_transform(features)

    selected_feat = [xAxis_feature, yAxis_feature]
    
    classify = classifier(filename, selected_feat)
    validate = validator(selected_feat, classify, k)
    
    predictions = []
    
    for i in range(len(data)):
        classify.train([j for j in range(len(data)) if j != i])
        pred = classify.test(i, k)
        print(pred[0][0])
        predictions.append(pred[0][0])
        
    x_vals = features[:, xAxis_feature - 1]
    y_vals = features[:, yAxis_feature - 1]

    # Color based on class label
    colors = ['red' if int(p) == 2 else 'blue' for p in predictions]

    plt.figure(figsize=(6, 6))
    plt.scatter(x_vals, y_vals, c=colors, edgecolor='k', alpha=0.6)
    plt.xlabel(f"Feature {xAxis_feature}")
    plt.ylabel(f"Feature {yAxis_feature}")
    plt.title(plotTitle)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def accuracyPlot(filename, selected_feat):
    k_vals = [1.3,5,7]
    
    accuracy = []

    for k in k_vals:
        classifiedK = classifier(filename, selected_feat)
        validatedK = validator(selected_feat, classifiedK, k)
        accuracyK = validatedK.validate()
        accuracy.append(accuracyK)
        
    plt.figure()
    plt.plot(k_vals, accuracy, marker = 'o')
    plt.title(f"KNN Accuracy (Forward Selection) ({filename})")
    plt.xlabel("K (Num of Neighbor)")
    plt.ylabel("Accuracy")
    plt.grid()
    plt.tight_layout()
    plt.show()







def main():
    print("Welcome to Dmitry Sorokin and Kyle Chahal's Feature Selection Algorithm")

    num_features = int(input("Please enter the total number of features: "))
    
    print("\n Type the number of the algorithm you want to run")
    print("1) Forward Selection")
    print("2) Backward Elimination")
    
    user_choice = int(input())
    
    if user_choice == 1:
        part1.forwardSel(num_features)
    elif user_choice == 2:
        part1.backwardsElim(num_features)
    else:
        print("Invalid Option")
        
def mainP3():
    print("Welcome to Dmitry Sorokin and Kyle Chahal's Feature Selection Algorithm\n\n")

    print(f"Here is a list of avaliable datasets:\n\t1) Small-Test-Dataset\n\t2) Large-Test-Dataset\n\t3) Titanic")
    dataset = int(input("Please choose the number of the dataset you would like to use:"))
    if(1 == dataset):
        filename = "small-test-dataset.txt"
    elif(2 == dataset):
        filename = "large-test-dataset.txt"
    elif(3 == dataset):
        filename = "titanic clean.txt"

    print("\n Type the number of the algorithm you want to run")
    print("1) Forward Selection")
    print("2) Backward Elimination")
    print("3: PLOTS")
    user_choice = int(input())

    k = int(input("Please enter the number of neighbors to compare to:"))
    
    if user_choice == 1:
        part3.forwardSel(filename, k)
    elif user_choice == 2:
        part3.backwardsElim(filename, k)
    elif user_choice == 3:
        print("\nPlotting accuracy vs. k for Titanic dataset...")

        # Replace these with your actual selected feature sets
        # forward_features = [2, 3]
        # backward_features = [1, 4]

        plot_feature_scatter("small-test-dataset.txt", 3, 5, "Small Dataset", k)
        #plot_feature_scatter("large-test-dataset.txt", 15, 27, "Large Dataset", k)
        accuracyPlot("titanic clean.txt", [2, 3])
    else:
        print("Invalid Option")

#main()
mainP3()
