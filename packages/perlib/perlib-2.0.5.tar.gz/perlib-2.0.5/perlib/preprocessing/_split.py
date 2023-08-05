import abc
import numpy as np

from sklearn.base import BaseEstimator
from sklearn.utils.validation import indexable
from sklearn.model_selection import train_test_split as tts

__all__ = [
    'check_cv',
    'train_test_split',
    'RollingForecastCV',
    'SlidingWindowForecastCV'
]


def train_test_split(*arrays,
                     test_size=None,
                     train_size=None,
                     random_state=123,
                     shuffle=False,
                     stratify=None
                     ):
    """Split arrays or matrices into sequential train and test subsets
    Creates train/test splits over endogenous arrays an optional exogenous
    arrays. This is a wrapper of scikit-learn's ``train_test_split`` that
    does not shuffle.
    Parameters
    ----------
    *arrays : sequence of indexables with same length / shape[0]
        Allowed inputs are lists, numpy arrays, scipy-sparse
        matrices or pandas dataframes.
    test_size : float, int or None, optional (default=None)
        If float, should be between 0.0 and 1.0 and represent the proportion
        of the dataset to include in the test split. If int, represents the
        absolute number of test samples. If None, the value is set to the
        complement of the train size. If ``train_size`` is also None, it will
        be set to 0.25.
    train_size : float, int, or None, (default=None)
        If float, should be between 0.0 and 1.0 and represent the
        proportion of the dataset to include in the train split. If
        int, represents the absolute number of train samples. If None,
        the value is automatically set to the complement of the test size.
    Returns
    -------
    splitting : list, length=2 * len(arrays)
        List containing train-test split of inputs.
    Examples
    --------
    """
    return tts(
        *arrays,
        random_state=123,
        shuffle=False,
        stratify=None,
        test_size=test_size,
        train_size=train_size)


class BaseTSCrossValidator(BaseEstimator, metaclass=abc.ABCMeta):
    """Base class for time series cross validators
    Based on the scikit-learn base cross-validator with alterations to fit the
    time series interface.
    """
    def __init__(self, h, step):
        if h < 1:
            raise ValueError("h must be a positive value")
        if step < 1:
            raise ValueError("step must be a positive value")

        self.h = h
        self.step = step

    @property
    def horizon(self):
        """The forecast horizon for the cross-validator"""
        return self.h

    def split(self, y, X=None):
        """Generate indices to split data into training and test sets
        Parameters
        ----------
        y : array-like or iterable, shape=(n_samples,)
            The time-series array.
        X : array-like, shape=[n_obs, n_vars], optional (default=None)
            An optional 2-d array of exogenous variables.
        Yields
        ------
        train : np.ndarray
            The training set indices for the split
        test : np.ndarray
            The test set indices for the split
        """
        y, X = indexable(y, X)
        indices = np.arange(y.shape[0])
        for train_index, test_index in self._iter_train_test_masks(y, X):
            train_index = indices[train_index]
            test_index = indices[test_index]
            yield train_index, test_index

    def _iter_train_test_masks(self, y, X):
        """Generate boolean masks corresponding to test sets"""
        for train_index, test_index in self._iter_train_test_indices(y, X):
            train_mask = np.zeros(y.shape[0], dtype=bool)
            test_mask = np.zeros(y.shape[0], dtype=bool)

            train_mask[train_index] = True
            test_mask[test_index] = True
            yield train_mask, test_mask

    @abc.abstractmethod
    def _iter_train_test_indices(self, y, X):
        """Yields the train/test indices"""


class RollingForecastCV(BaseTSCrossValidator):
    """Use a rolling forecast to perform cross validation
    Sometimes called “evaluation on a rolling forecasting origin” [1], this
    approach to CV incrementally grows the training size while using a single
    future sample as a test sample, e.g.:
    With h == 1::
        array([15136., 16733., 20016., 17708., 18019., 19227., 22893., 23739.])
        1st: ~~~~ tr ~~~~ tr ~~~~ te
        2nd: ~~~~ tr ~~~~ tr ~~~~ tr ~~~~ te
        3rd: ~~~~ tr ~~~~ tr ~~~~ tr ~~~~ tr ~~~~ te
    With h == 2::
        array([15136., 16733., 20016., 17708., 18019., 19227., 22893., 23739.])
        1st: ~~~~ tr ~~~~ tr ~~~~ te ~~~~ te
        2nd: ~~~~ tr ~~~~ tr ~~~~ tr ~~~~ te ~~~~ te
        3rd: ~~~~ tr ~~~~ tr ~~~~ tr ~~~~ tr ~~~~ te ~~~~ te
    Parameters
    ----------
    h : int, optional (default=1)
        The forecasting horizon, or the number of steps into the future after
        the last training sample for the test set.
    step : int, optional (default=1)
        The size of step taken to increase the training sample size.
    initial : int, optional (default=None)
        The initial training size. If None, will use 1 // 3 the length of the
        time series.
    Examples
    --------
    With a step size of one and a forecasting horizon of one, the training size
    will grow by 1 for each step, and the test index will be 1 + the last
    training index:
    """
    def __init__(self, h=1, step=1, initial=None):
        super().__init__(h, step)
        self.initial = initial

    def _iter_train_test_indices(self, y, X):
        """Yields the train/test indices"""
        n_samples = y.shape[0]
        initial = self.initial
        step = self.step
        h = self.h

        if initial is not None:
            if initial < 1:
                raise ValueError("Initial training size must be a positive "
                                 "integer")
            elif initial + h > n_samples:
                raise ValueError("The initial training size + forecasting "
                                 "horizon would exceed the length of the "
                                 "given timeseries!")
        else:
            # if it's 1, we have another problem..
            initial = max(1, n_samples // 3)

        # Determine the number of iterations that will take place. Must
        # guarantee that the forecasting horizon will not over-index the series
        all_indices = np.arange(n_samples)
        window_start = 0
        window_end = initial
        while True:
            if window_end + h > n_samples:
                break

            train_indices = all_indices[window_start: window_end]
            test_indices = all_indices[window_end: window_end + h]
            window_end += step

            yield train_indices, test_indices


class SlidingWindowForecastCV(BaseTSCrossValidator):
    """Use a sliding window to perform cross validation
    This approach to CV slides a window over the training samples while using
    several future samples as a test set. While similar to the
    :class:`RollingForecastCV`, it differs in that the train set does not grow,
    but rather shifts.
    Parameters
    ----------
    h : int, optional (default=1)
        The forecasting horizon, or the number of steps into the future after
        the last training sample for the test set.
    step : int, optional (default=1)
        The size of step taken between training folds.
    window_size : int or None, optional (default=None)
        The size of the rolling window to use. If None, a rolling window of
        size n_samples // 5 will be used.
    Examples
    --------
    """
    def __init__(self, h=1, step=1, window_size=None):
        super().__init__(h, step)
        self.window_size = window_size

    def _iter_train_test_indices(self, y, X):
        """Yields the train/test indices"""
        n_samples = y.shape[0]
        window_size = self.window_size
        step = self.step
        h = self.h

        if window_size is not None:
            if window_size + h > n_samples:
                raise ValueError("The window_size + forecasting "
                                 "horizon would exceed the length of the "
                                 "given timeseries!")
        else:
            # TODO: what's a good sane default for this?
            window_size = max(3, n_samples // 5)

        if window_size < 3:
            raise ValueError("window_size must be > 2")

        indices = np.arange(n_samples)
        window_start = 0
        while True:
            window_end = window_start + window_size
            if window_end + h > n_samples:
                break

            train_indices = indices[window_start: window_end]
            test_indices = indices[window_end: window_end + h]
            window_start += step

            yield train_indices, test_indices


def check_cv(cv=None):
    """Input checker utility for building a cross-validator
    Parameters
    ----------
    cv : BaseTSCrossValidator or None, optional (default=None)
        An instance of CV or None. Possible inputs:
        - None, to use a default RollingForecastCV
        - A BaseTSCrossValidator as a passthrough
    """
    cv = RollingForecastCV() if cv is None else cv
    if not isinstance(cv, BaseTSCrossValidator):
        raise TypeError("cv should be an instance of BaseTSCrossValidator or "
                        "None, but got %r (type=%s)" % (cv, type(cv)))
    return cv