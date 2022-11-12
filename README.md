# AutoML
    # data used was from surveys from the speech language patholgist
    # 
5. In a markdown file (readme.md): 
    - Describe the two dependent variables (outcomes) for experiment 1 and experiment 2
        # Regressional: Years worked in both medical and educational settings (Q_40_3) (continous)
            # I inseted another column in the excel to sum up years worked in both settings 
        # Classification: The variable here was a categorical one for wether or not SPLs choose this career as their first choice (Q43) to see if it correlated to the responsese they have
    
    - Describe for each experiment: 
        - What was the best performing model (please interpret (a) log-loss or RMSE between models, and (b) AUC)
        # Regressional:
            # best model was the linear model with a RMSE of 0.0000000000000236996 or 2.36996^-10 
        # Classification:
            # The ensemble model worked the best for the the classifaction with a log loss of 0.508274 and a auc of 0.84444 and the Xgboost came very close to the ensemble model
        - How much better (? if any) did the model perform compared to baseline
        # For the classification up to two models did better then the baseline and ensemble.
        # For regressional 5 out of the 6 models did better then base line with the only outlier being the neural network