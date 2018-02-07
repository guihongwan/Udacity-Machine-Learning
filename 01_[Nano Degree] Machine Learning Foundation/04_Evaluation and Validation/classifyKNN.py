def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    
    ### your code goes here!
    
    from sklearn.neighbors import KNeighborsClassifier
    n_neighbors = 1
    clf = KNeighborsClassifier(n_neighbors)#weights = 'distance'
    clf.fit(features_train, labels_train)
    return clf
    
    
    