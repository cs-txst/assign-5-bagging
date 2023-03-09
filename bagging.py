from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.base import clone
import numpy as np
import random



class CustomBaggingClassifier(BaseEstimator, ClassifierMixin):

    def __init__(self, base_estimator=None, n_estimators=10, random_state=None):
        """
        Parameters
        ----------
        base_estimator : object or None, optional (default=None)     The base estimator to fit on random subsets of the dataset. If None, then the base estimator is a decision tree.
        n_estimators : int, optional (default=10)                     The number of base estimators in the ensemble.
        random_state : int, RandomState instance or None, optional (default=None)  Controls the randomness of the 
            estimator. The features are always randomly permuted at each split, even if splitter is set to "best". 
            When max_features < n_features, the algorithm will select max_features at random at each split before finding the best split among them. But the best found split may vary across different runs, even if max_features=n_features. That is the case, if the improvement of the criterion is identical for several splits and one split has to be selected at random. To obtain a deterministic behaviour during fitting, random_state has to be fixed to an integer.
        """

        #TODO: ...



    def fit(self, X, y):
        """
        Build a Bagging classifier from the training set (X, y).
        
        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)                  The input samples.
        y : ndarray of shape (n_samples,)                             The target values.
        
        Returns
        -------
        self : object
            Returns self.
        """

        # Check that X and y have correct shape
        X, y = check_X_y(X, y)

        # Store the classes seen during fit
        self.classes_ = unique_labels(y)

        #TODO: ...

        # Return the classifier
        return self
    

    def predict(self, X):
        """
        Predict class for X.
        
        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)                  The input samples.
        
        Returns
        -------
        pred : ndarray of shape (n_samples,)                          The predicted classes.
        """

        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        #TODO: ...

        return pred


    def predict_proba(self, X):
        """
        Predict class probabilities for X.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)      The input samples.

        Returns
        -------
        probas : ndarray of shape (n_samples, n_classes)  The class probabilities of the input samples. The order of 
            the classes corresponds to that in the attribute classes_.
        """

        # Check is fit had been called
        check_is_fitted(self)

        # Input validation
        X = check_array(X)

        #TODO: ...

        return probas


    def _get_bootstrap_sample(self, X, y):
        """
        Returns a bootstrap sample of the same size as the original input X, 
        and the out-of-bag (oob) sample. According to the theoretical analysis, about 63.2% 
        of the original indexes will be included in the bootsrap sample. Some indexes will
        appear multiple times.
        
        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)                  The input samples.
        y : ndarray of shape (n_samples,)                             The target values.

        Returns
        -------
        bootstrap_sample_X : ndarray of shape (n_samples, n_features) The bootstrap sample of the input samples.
        bootstrap_sample_y : ndarray of shape (n_samples,)            The bootstrap sample of the target values.
        oob_sample_X : ndarray of shape (n_samples, n_features)       The out-of-bag sample of the input samples.
        oob_sample_y : ndarray of shape (n_samples,)                  The out-of-bag sample of the target values.
        """

        # Check that X and y have correct shape
        X, y = check_X_y(X, y)

        #TODO: ...

        return bootstrap_sample_X, bootstrap_sample_y, oob_sample_X, oob_sample_y

