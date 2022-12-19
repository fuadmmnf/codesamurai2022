import json
from api.models import Project

projects = json.load(open('api/seed/projects.json'))
for project in projects:
    Project(
        project_name=project['project_name'],
        category=project['category'],
        affiliated_agency=project['affiliated_agency'],
        description=project['description'],
        project_start_time=project['project_start_time'],
        project_completion_time=project['project_completion_time'],
        total_budget=project['total_budget'],
        completion_percentage=project['completion_percentage'],
        location_coordinates=project['location_coordinates'],
    ).save()
