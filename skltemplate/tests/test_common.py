import pytest

from sklearn.utils.estimator_checks import check_estimator

from skltemplate import TemplateEstimator
from skltemplate import TemplateClassifier
from skltemplate import TemplateTransformer


@pytest.mark.parametrize(
    "estimator",
    [TemplateEstimator(), TemplateTransformer(), TemplateClassifier()]
)
def test_all_estimators(estimator):
    return check_estimator(estimator)
