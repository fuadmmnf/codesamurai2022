import json
from api.models import *
from datetime import datetime

roles = json.load(open('api/seed/data/user_types.json'))
UserType.objects.all().delete()
for role in roles:
    UserType(
        code=role['code'],
        committee=role['committee'],
        description=role['description'],
    ).save()

agencies = json.load(open('api/seed/data/agencies.json'))
Agency.objects.all().delete()
for agency in agencies:
    Agency(
        code=agency['code'],
        name=agency['name'],
        type=agency['type'],
        description=agency['description'],
    ).save()

projects = json.load(open('api/seed/data/projects.json'))
Project.objects.all().delete()
for project in projects:
    Project(
        project_id=project['project_id'],
        exec=Agency.objects.get(code__exact=project['exec']),
        project_name=project['project_name'],
        location=project['location'],
        start_date=datetime.strptime(project['start_date'], "%Y-%m-%d"),
        total_budget=project['total_budget'],
        latitute=project['latitute'],
        longitude=project['longitude'],
        cost=project['cost'],
        timespan=project['timespan'],
        goal=project['goal'],
        completion=project['completion'],
        actual_cost=project['actual_cost'],
    ).save()

components = json.load(open('api/seed/data/components.json'))
Component.objects.all().delete()
for component in components:
    Component(
        component_id=component['component_id'],
        project_id=Project.objects.get(project_id__exact=component['project_id']),
        execution_agency=Agency.objects.get(code__exact=component['execution_agency']),
        component_type=component['component_type'],
        depends_on=None if len(component['depends_on']) < 1 else Component.objects.get(
            component_id__exact=component['depends_on']),
        budget_ratio=component['budget_ratio'],
    ).save()

proposals = json.load(open('api/seed/data/proposals.json'))
for proposal in proposals:
    Project(
        project_id=proposal['project_id'],
        exec=Agency.objects.get(code__exact=proposal['exec']),
        project_name=proposal['project_name'],
        location=proposal['location'],
        proposal_date=datetime.strptime(proposal['proposal_date'], "%Y-%m-%d"),
        total_budget=proposal['total_budget'],
        latitute=proposal['latitute'],
        longitude=proposal['longitude'],
        cost=proposal['cost'],
        timespan=proposal['timespan'],
        goal=proposal['goal'],
        is_accepted=False,
    ).save()


constraints = json.load(open('api/seed/data/constraints.json'))
Constraint.objects.all().delete()
for constraint in constraints:
    Constraint(
        constraint_tyoe=constraint['constraint_type'],
        code=constraint['code'],
        max_limit=constraint['max_limit'],
    ).save()
