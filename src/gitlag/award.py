import os
import gitlab
import gitlab.v4.objects


def get_gitlab_api():
    gitlab_url = os.environ.get("GITLAB_URL", "https://gitlab.be-md.ncbi.nlm.nih.gov/")
    token = os.environ.get("GITLAB_TOKEN")
    return gitlab.Gitlab(gitlab_url, token)


def award_for_mr(gl, emoji_name, project_id, mr_id):
    project = gl.projects.get(project_id, lazy=True)
    mr = project.mergerequests.get(mr_id, lazy=True)
    mr.awardemojis.create({'name': emoji_name})


# emoji names in https://raw.githubusercontent.com/bonusly/gemojione/master/config/index.json
# award_for_mr(get_gitlab_api(), "apple", 8532, 1)
