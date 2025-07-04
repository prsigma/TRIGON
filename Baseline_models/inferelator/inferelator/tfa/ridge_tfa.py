from .tfa_base import ActivityOnlyTFA
from sklearn.linear_model import Ridge
from inferelator.utils.sparse import todense


class _Ridge_TFA_mixin:
    """
    TFA calculates transcription factor activity
    using ridge regression

    Constrained to positive values
    """

    @staticmethod
    def _calculate_activity(
        prior,
        expression_data
    ):

        ridge_regressor = Ridge(
            alpha=0.01,
            fit_intercept=False,
            solver='lbfgs',
            positive=True
        )

        ridge_regressor.fit(
            prior,
            todense(expression_data).T
        )

        return ridge_regressor.coef_.copy()


class RidgeTFA(_Ridge_TFA_mixin, ActivityOnlyTFA):
    pass
