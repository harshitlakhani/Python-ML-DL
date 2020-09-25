
import pandas as pd
from sklearn import ensemble
from sklearn import preprocessing
from sklearn import metrics
import pickle
import sys
import dispatcher

TRAINING_DATA = sys.argv[1]
TEST_DATA = sys.argv[2]
MODEL = sys.argv[3]

FOLD_MAPPPING = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3]
}

if __name__ == "__main__":
    df = pd.read_csv(TRAINING_DATA)
    df_test = pd.read_csv(TEST_DATA)
    for FOLD in range(5):
        train_df = df[df.kfold.isin(FOLD_MAPPPING.get(FOLD))].reset_index(drop=True)
        valid_df = df[df.kfold==FOLD].reset_index(drop=True)

        ytrain = train_df.target.values
        yvalid = valid_df.target.values

        train_df = train_df.drop(["id", "target", "kfold"], axis=1)
        valid_df = valid_df.drop(["id", "target", "kfold"], axis=1)

        valid_df = valid_df[train_df.columns]

        label_encoders = {}
        for c in train_df.columns:
            lbl = preprocessing.LabelEncoder()
            train_df.loc[:, c] = train_df.loc[:, c].astype(str).fillna("NONE")
            valid_df.loc[:, c] = valid_df.loc[:, c].astype(str).fillna("NONE")
            df_test.loc[:, c] = df_test.loc[:, c].astype(str).fillna("NONE")
            lbl.fit(train_df[c].values.tolist() + 
                    valid_df[c].values.tolist() + 
                    df_test[c].values.tolist())
            train_df.loc[:, c] = lbl.transform(train_df[c].values.tolist())
            valid_df.loc[:, c] = lbl.transform(valid_df[c].values.tolist())
            label_encoders[c] = lbl
        
        # data is ready to train
        clf = dispatcher.models[MODEL]
        clf.fit(train_df, ytrain)
        preds = clf.predict_proba(valid_df)[:, 1]
        print(f"ROC-AUC for fold {FOLD}" , metrics.roc_auc_score(yvalid, preds))

        pickle.dump(label_encoders, open(f"../models/{MODEL}_{FOLD}_label_encoder.pkl","wb"))
        pickle.dump(clf, open(f"../models/{MODEL}_{FOLD}.pkl","wb"))
        pickle.dump(train_df.columns, open(f"../models/{MODEL}_{FOLD}_columns.pkl","wb"))