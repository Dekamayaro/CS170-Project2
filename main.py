import node
import validator
import classifier
import part1
import random

def main():
    random.seed(0)
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
        
        

main()

