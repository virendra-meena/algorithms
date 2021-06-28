"""
feature importance- (from kaggle)
    1. permutation importance --
            1.  need a trained model
            2.  randomly shuffles/permute a column in validation dataset, keeping other columns intact.
            3. chekc the accuracy on new validation dataset, if the feature is considered important by model, it will reduce the accuracy.

    2. partial dependency plots:
            1. need a trained model again.
            2. for a single row, change the value of a feature in a range [start, stop], and observe the impact of changes.
            3.

    3. shap values:
            1. shap values provide insight on how much a feature value contributed in prediction w.r.t the baseline value.
            2. num_of_goal being a feature, having value=3 versus baseline=1, how much it contribute to label (man_of_the_match)


decision trees (from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor)
    1. easier to explain -- explainability for practitioners
    2. classification - gini_index
    3. regression -  mean_squared_error




Weak learners can be combined to get a model with better performances.
The way to combine base models should be adapted to their types.
Low bias and high variance weak models should be combined in a way that makes the strong model more robust whereas
low variance and high bias base models better be combined in a way that makes the ensemble model less biased.

bagging -- to reduce variance
boosting-- to reduce bias

"""