import time
from validator import validator
from classifier import classifier

def run_validation(fileName, feature_subset):
    for feat in feature_subset:
        print(f"Evaluating Feature Set: {feat}")
        classif = classifier(fileName, selected_feat = feat)
        validate = validator(features = feat, Classifier= classif, filename = fileName)
        
        starting_Time = time.time()
        accuracy = validate.validate()
        ending_time = time.time()
        
        print(f"Leave one out accuracy: {accuracy}")
        print(f"Time taken: {ending_time - starting_Time} seconds\n")
        

run_validation("large-test-dataset.txt", [[1, 15, 27]])