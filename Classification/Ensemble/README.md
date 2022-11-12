# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model             |   Weight |
|:------------------|---------:|
| 1_Baseline        |        1 |
| 4_Default_Xgboost |        5 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.508274 | nan         |
| auc       | 0.844444 | nan         |
| f1        | 0.666667 |   0.131913  |
| accuracy  | 0.785714 |   0.212172  |
| precision | 1        |   0.399488  |
| recall    | 1        |   0.0881909 |
| mcc       | 0.547723 |   0.399488  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.508274 |  nan        |
| auc       | 0.844444 |  nan        |
| f1        | 0.666667 |    0.212172 |
| accuracy  | 0.785714 |    0.212172 |
| precision | 0.75     |    0.212172 |
| recall    | 0.6      |    0.212172 |
| mcc       | 0.518545 |    0.212172 |


## Confusion matrix (at threshold=0.212172)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                8 |                1 |
| Labeled as 1 |                2 |                3 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
