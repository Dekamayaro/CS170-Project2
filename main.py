import node
import validator
import classifier
import part1
import part3

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

    print(f"Here is a list of avaliable dataasets:\n\t1) Small-Test-Dataset\n\t2) Large-Test-Dataset")
    dataset = int(input("Please choose the number of the dataset you would like to use:"))
    if(1 == dataset):
        filename = "small-test-dataset.txt"
    elif(2 == dataset):
        filename = "large-test-dataset.txt"

    print("\n Type the number of the algorithm you want to run")
    print("1) Forward Selection")
    print("2) Backward Elimination")
    
    user_choice = int(input())
    
    if user_choice == 1:
        part3.forwardSel(filename)
    elif user_choice == 2:
        part3.backwardsElim(filename)
    else:
        print("Invalid Option")


#main()
mainP3()

