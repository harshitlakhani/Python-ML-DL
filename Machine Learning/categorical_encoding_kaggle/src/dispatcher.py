from sklearn import ensemble
models = {
    "randomforest" : ensemble.RandomForestClassifier(n_estimators = 100, n_jobs=-1, verbose=2),
    "extratrees" : ensemble.ExtraTreesClassifier(n_estimators =  0, n_jobs=-1, verbose=2),
}