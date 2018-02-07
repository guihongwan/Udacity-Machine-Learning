def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    
    import numpy as np
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split = 50)
    clf.fit(features_train, labels_train)
    return clf
    
    
    