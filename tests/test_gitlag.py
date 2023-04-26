from unittest.mock import Mock
from gitlag.award import award_for_mr


def test_award_for_mr_mock_gl():
    """
    Test that award_for_mr function calls appropriate GitLab python api functions.
    Mock gitlab_api and project objects.
    """
    gl_mock = Mock(name="mymock")

    # don't do this:
    # project_mock = Mock()
    # gl_mock.project.get.return_value = project_mock

    award_for_mr(gl_mock, "baloon", 12, 5)
    # assert gl_mock functions called - see https://docs.python.org/3/library/unittest.mock-examples.html#mocking-chained-calls

    assert gl_mock.projects.get.called_once
    assert gl_mock.projects.get.call_args.args == (12, )

    print(gl_mock.projects.get)

    assert gl_mock.projects.get.return_value.mergerequests.get.called_once
    assert gl_mock.projects.get.return_value.mergerequests.get.call_args.args == (5, )

    assert gl_mock.projects.get.return_value.mergerequests.get.return_value.awardemojis.create.called_once
    assert gl_mock.projects.get.return_value.mergerequests.get.return_value.awardemojis.create.call_args.args == ({"name": "baloon"}, )

    assert False