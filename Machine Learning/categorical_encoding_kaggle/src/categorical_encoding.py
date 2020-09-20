from sklearn import preprocessing

class CategoricalEncoding():
    def __init__(
        self,
        dataframe,
        categrical_features,
        encoding_type,
        handle_na = False
    ):
        self.dataframe = dataframe
        self.features = categrical_features
        self.encoding = encoding_type
        self.handle_na = handle_na
        self.label_encoder = dict()
        self.binary_encoder = dict()
        self.ohe = None

        if self.handle_na == True:
            for f in features:
                self.dataframe.loc[:,c] = self.dataframe.loc[:,f].astype("str").fillna("-9999999")
        self.final_dataframe = self.dataframe.copy(deep=True)

    def _label_encoding(self):
        for c in self.features:
            lbl = preprocessing.LabelEncoder()
            lbl.fit(self.dataframe[c].values)
            self.final_dataframe.loc[:,c] = lbl.transform(self.dataframe[c].values)
            self.label_encoder[c] = lbl
        return self.final_dataframe

    def _binary_encoding(self):
        for c in self.features:
            lbl = preprocessing.LabelBinarizer()
            lbl.fit(self.dataframe[c].values)
            ary = lbl.transform(self.df[c].values)
            self.final_dataframe.drop(c, inplace=True)
            for j in range(ary.shape[1]):
                new_bin_col = c + f"_bin_{j}"
                self.final_dataframe[new_bin_col] = ary[:,j]
            self.binary_encoder[c] = lbl
        return self.final_dataframe

    def _one_hot_encofing(self):
        ohe = preprocessing.OneHotEncoder()
        ohe.fit(self.dataframe[self.features].values)
        return ohe.transform(self.dataframe[self.features].values)

    def fit_transform(self):
        if self.encoding == "label":
            return self._label_encoding()
        elif self.encoding == "binary":
            return self._binary_encoding()
        elif self.encoding == "onehot":
            return self._one_hot_encofing()
        else:
            raise Exception("Encoding type is not understtod!!")

    def transform(self, dataframe):
        if self.handle_na == True:
            for f in features:
                dataframe.loc[:,c] = dataframe.loc[:,f].astype("str").fillna("-9999999")
        
        if self.encoding == "label":
            for c, lbl in self.label_encoder.items():
                dataframe.loc[:,c] = lbl.transform(dataframe.loc[:,c].values)
            return dataframe
        
        elif self.encoding == "binary":
            for c, lbl in self.binary_encoder.items():
                ary = lbl.transform(self.dataframe[c].values)
                self.dataframe.drop(c, inplace=True)
                for j in range(ary.shape[1]):
                    new_bin_col = c + f"_bin_{j}"
                    self.dataframe[new_bin_col] = ary[:,j]
            return dataframe

        elif self.encoding == "ohe":
            return self.ohe.transform(dataframe[self.features].values)

        else:
            raise Exception("Label type is not understood!!")
                

if __name__ = "__main__":
    import pandas as pd
    from sklearn import linear_model

    df_train = pd.read_csv("../input/train.csv") # for handing unseen test data we have to make some changes in this code
    col = [c for c in df_train.columns if c not in ["id","target"]]
    cat_feat = CategoricalEncoding(
        dataframe = df_train,
        categorical_features = col,
        encoding_type = "label",
        handle_na = True
    )
    transformed_data = cat_feat.fit_transform()