from  api.models import *
import pandas as pd
from datetime import datetime


def resync_db():
    projects_df = pd.DataFrame(list(Project.objects.filter(is_accepted=True).all().values()))
    proposals_df = pd.DataFrame(list(Project.objects.filter(is_accepted=False).all().values()))
    components_df = pd.DataFrame(list(Component.objects.all().values()))
    constraints_df = pd.DataFrame(list(Constraint.objects.all().values()))
    agencies_df = pd.DataFrame(list(Agency.objects.all().values()))

    updated_projects_list = []
    updated_proposals_list = []

    for updated_project in updated_projects_list:
        project = Project.objects.get(project_id__exact=updated_project['project_id'])
        project.est_completion_date = datetime.strptime(updated_project['est_completion_date'], "%Y-%m-%d"),
        project.save()

    for updated_proposal in updated_proposals_list:
        proposal = Project.objects.get(project_id__exact=updated_proposal['project_id'])
        proposal.est_completion_date = datetime.strptime(updated_proposal['est_completion_date'], "%Y-%m-%d")
        proposal.save()
