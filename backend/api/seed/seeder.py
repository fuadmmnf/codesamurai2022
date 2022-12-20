import pandas as pd
from api.models import *
from datetime import datetime

roles = pd.read_csv(open('api/seed/data/user_types.csv'))
UserType.objects.all().delete()
User.objects.all().delete()
for i, role in roles.iterrows():
    UserType(
        code=role['code'],
        committee=role['committee'],
        description=role['description'],
    ).save()

    User(
        username=role['code'],
        password=hash('secret123'),
        user_type=UserType.objects.get(code__exact=role['code']),
    ).save()

agencies = pd.read_csv(open('api/seed/data/agencies.csv'))
Agency.objects.all().delete()
for i, agency in agencies.iterrows():
    Agency(
        code=agency['code'],
        name=agency['name'],
        type=agency['type'],
        description=agency['description'],
    ).save()

projects = pd.read_csv(open('api/seed/data/projects.csv'))
Project.objects.all().delete()
for i, project in projects.iterrows():
    Project(
        project_id=project['project_id'],
        exec=Agency.objects.get(code__exact=project['exec']),
        project_name=project['name'],
        location=project['location'],
        start_date=datetime.strptime(project['start_date'], "%Y-%m-%d"),
        latitude=project['latitude'],
        longitude=project['longitude'],
        cost=project['cost'],
        timespan=project['timespan'],
        goal=project['goal'],
        completion=project['completion'],
        actual_cost=project['actual_cost'],
    ).save()


proposals = pd.read_csv(open('api/seed/data/proposals.csv'))
for i, proposal in proposals.iterrows():
    Project(
        project_id=proposal['project_id'],
        exec=Agency.objects.get(code__exact=proposal['exec']),
        project_name=proposal['name'],
        location=proposal['location'],
        proposal_date=datetime.strptime(proposal['proposal_date'], "%Y-%m-%d"),
        latitude=proposal['latitude'],
        longitude=proposal['longitude'],
        cost=proposal['cost'],
        timespan=proposal['timespan'],
        goal=proposal['goal'],
        is_accepted=False,
    ).save()

components = pd.read_csv(open('api/seed/data/components.csv'))
Component.objects.all().delete()
for i, component in components.sort_values(by='depends_on', ascending=False)[::-1].iterrows():
    Component(
        component_id=component['component_id'],
        project_id=Project.objects.get(project_id__exact=component['project_id']),
        executing_agency=Agency.objects.get(code__exact=component['ececuting_agency']),
        component_type=component['component_type'],
        depends_on=None if pd.isna(component['depends_on']) else Component.objects.get(
            component_id__exact=component['depends_on']),
        budget_ratio=component['budget ratio'],
    ).save()


constraints = pd.read_csv(open('api/seed/data/constraints.csv'))
Constraint.objects.all().delete()
for i, constraint in constraints.iterrows():
    Constraint(
        constraint_type=constraint['constraint_type'],
        code=constraint['code'],
        max_limit=constraint['max_limit'],
    ).save()

