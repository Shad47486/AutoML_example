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

mldata = pd.read_csv('dataset\SPL.csv')
mldata
mldata.columns
print(mldata)
# variables of interest from dataset 
    ## I feel Emotionally drained from work? (categorical) (Q11)
    ## how many years worked in both settings? (continous) (Q_40_3)
    ## Was becoming a speech-language pathologist your first career choice? (categorical) (Q43)
        ## looking to see if their is a trend with feeling emotionally drained and --
        ## -- years worked in the industry
#cleaning data 
mldata = mldata.drop([0], axis=0)
    #gets rid question row 
mldata['Q43'].describe()
mldata['Q_40_3'].describe()
mldata['Q11'].value_counts()

mldata['Q43'] = pd.to_numeric(mldata['Q43'], errors='coerce')
mldata['Q43v2'] = mldata['Q43'].apply(lambda x: '0' if x == 'Yes' else '1')
mldata.drop('Q43', axis=1, inplace=True)
mldata['Q43v2'].value_counts()

X = mldata.drop(columns=['Q43v2'])
y = mldata["Q43v2"]
X
y
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.25)
X_test


automl = AutoML(results_path="Classification", mode="Explain")
automl.fit(X_train, y_train)
pred = automl.predict(X_test)
pred
automl.report()

# loading in the new data model
automl_mldata_q43 = AutoML(results_path="Classification")
X_withq43 = mldata.sample(25)
X_withoutq43 = X_withq43.drop(columns=['Q43v2'])
X_withq43
X_withoutq43
predict = automl.predict(X_withoutq43)
predict

values_actual = X_withq43['Q43v2'].values.tolist()
values_predicted = predict.tolist()
output = pd.DataFrame({'actual': values_actual, 'predicted': values_predicted})
output