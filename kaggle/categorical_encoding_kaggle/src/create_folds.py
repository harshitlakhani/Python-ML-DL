#!python

import sys
import pandas as pd
from sklearn import model_selection

train_data = str(sys.argv[1])

if __name__ == '__main__':
    df =pd.read_csv(train_data)
    df["kfold"] = -1

    df = df.sample(frac=1).reset_index(drop=True)

    kf = model_selection.StratifiedKFold(n_splits=5, shuffle=False, random_state=34)

    for fold,(train_idx, validation_idx) in enumerate(kf.split(X=df, y=df.target.values)):
        df.loc[validation_idx, 'kfold'] = fold

df.to_csv('../input/train_folds.csv',index=False)