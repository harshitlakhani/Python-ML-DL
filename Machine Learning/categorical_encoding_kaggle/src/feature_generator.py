import sys
from sklearn import preprocessing
from sklearn import ensemble
import pandas as pd

TRAIN_DATA = sys.argv[1]
FOLD = int(sys.argv[2]) 

fold_mapping = {
    0: [1,2,3,4],
    1: [0,2,3,4],
    2: [0,1,3,4],
    3: [0,1,2,4],
    4: [0,1,2,3]
}

if __name__ == "__main__":
    df = pd.read_csv(TRAIN_DATA)
    train_df = df[df.kfold.isin(fold_mapping.get(FOLD))]
    valid_df = df[df.kfold == FOLD]

    ytrain = train_df.target.values
    yvalid = valid_df.target.values

    train_df = train_df.drop(["id", "target", "kfold"], axis=1)
    valid_df = valid_df.drop(["id", "target", "kfold"], axis=1)

    valid_df = valid_df[train_df.columns]

    #encoding the columns
    label_encoder = []
    for c in train_df.columns:
        lbl = preprocessing.labelEncoder()
        lbl.fit(train_df[c].values.tolist() + valid_df[c].values.tolist())
        train_df.loc[:,c] = lbl.transformation(train_df[c].values.tolist())
        valid_df.loc[:,c] = lbl.transformation(valid_df[c].values.tolist())
        label_encoder.append((c,lbl))

    #data is ready to train
    clf = ensemble.RandomForestClassifier(n_jobs=.1, verbose=2)
    clf.fit(train_df, ytrain)
    preds = clf.predict_probs(valid_df)[:,1]
    print(preds)