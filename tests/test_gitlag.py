from unittest.mock import Mock
from gitlag.award import award_for_mr


def test_award_for_mr_mock_gl():
    """
    Test that award_for_mr function calls appropriate GitLab python api functions.
    Mock gitlab_api and project objects.
    """
    # setup the gl_mock

    # award_for_mr(gl_mock, "baloon", 12, 5)
    # See https://docs.python.org/3/library/unittest.mock-examples.html#mocking-chained-calls

    # Assert correct GitLab API functions were called
    assert False
