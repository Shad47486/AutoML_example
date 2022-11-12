#pip install tpot mljar-supervised 
#this installs the needed ml modules for this assigment
#import needed modules
import os
import warnings
import supervised
from supervised import AutoML
from supervised.exceptions import AutoMLException
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
from sklearn import datasets
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
import pandas as pd

df = pd.read_csv("dataset\SPLv2.csv")
x_cols = [c for c in df.columns if c != "Q_40_3"] 
#Q_40_3 is the sum of years worked including both educational and medical settings
X = df[x_cols]
y = df["Q_40_3"]
df
x_cols
X
y
automl = AutoML(results_path="Regressional")
automl.fit(X, y)
df["predictions"] = automl.predict(X)
print(df["predictions"])
print(df[["Q_40_3", "predictions"]].head())

automl_q40 = AutoML(results_path="Regressional")
X_withq40 = df.sample(25)
X_withoutq40 = X_withq40.drop(columns=['Q_40_3'])
predict = automl.predict(X_withoutq40)
predict
values_actual = X_withq40['Q_40_3'].values.tolist()
values_predicted = predict.tolist()
output = pd.DataFrame({'actual': values_actual, 'predicted': values_predicted})
output
#exactly the same from actual and predicted

