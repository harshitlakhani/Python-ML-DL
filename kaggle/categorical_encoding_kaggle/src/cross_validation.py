import pandas as pd
from sklearn import model_selection


"""
-binary classification
-multiclass classification
-single column regression
"""


class CrossValidation():
    def __init__(
        self,
        df,
        target_cols,
        problem_type = "binary-classification",
        nfold = 5,
        shuffle = False,
        random_state = 42
    ):
        self.dataframe = df
        self.target_cols = target_cols
        self.num_targets  = len(self.target_cols)
        self.problem_type = problem_type
        self.nfold = nfold
        self.shuffle = shuffle
        self.random_state = random_state

        if self.shuffle == True:
            self.dataframe = self.dataframe.sample(frac=1).reset_index(drop=True)
        self.dataframe["kfold"] = -1

    def split(self):
        if self.problem_type in ["binary-classification","multiclass-classification"]:
            unique_values = self.dataframe[self.target_cols[0]].nunique() 
            if unique_values == 1:
                raise Exception("Only one unique value available")
            elif unique_values > 1:
                kf = model_selection.StratifiedKFold(
                    n_splits = self.nfold,
                    shuffle = False
                ) 
                for fold, (train_ind,val_ind) in enumerate(kf.split(X=self.dataframe, y=self.dataframe[self.target_cols[0]])):
                    self.dataframe.loc[val_ind,"kfold"] = fold
        return self.dataframe

        elif self.problem_type in ["single_col_regression","multi_col_regression"]:
            if self.num_targets != 1 and self.problem_type == "single_col_regression":
                raise Exception("Invalid number of targets for this problem type")
            elif self.num_targets < 2 and self.problem_type == "multi_col_regression":
                raise Exception("Invalid number of targets for this problem type")
            kf = model_selection.KFold(n_splits = self.nfold)
            for fold, (train_ind, valid_ind) in enumerate(kf.split(X = self.dataframe)):
                self.dataframe.loc[valid_ind, "kfold"] = fold

        elif self.problem_type.startswith("holdout_"):
            percentage = self.problem_type.split("_")[1]
            cutoff = int((len(self.dataframe)*percentage)/100)
            self.dataframe.loc[:len(self.dataframe) - cutoff, "kfold"] = 0
            self.dataframe.loc[len(self.dataframe) - cutoff:, "kfold"] = 1
        
        elif self.problem_type == "multi_label_classification":
            if self.num_targets != 1:
                raise Exception("Invalid number of targets for this problem type")
            targets = self.dataframe.["target"].apply(lambda x: len(str(x).split(self.delimiter)))
            kf = model_selection.StratifiedKFold(
                    n_splits = self.nfold
                ) 
            for fold, (train_ind,val_ind) in enumerate(kf.split(X=self.dataframe, y=targets)):
                self.dataframe.loc[val_ind,"kfold"] = fold
        
        else:
             raise Exception("Problem type not understood!!")



if __name__ =="__main__":
    df = pd.read_csv('../input/train.csv')
    cv = CrossValidation(df, target_cols=["target"])
    df_split = cv.split()
