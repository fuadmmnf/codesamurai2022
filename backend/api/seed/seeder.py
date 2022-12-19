import json
from api.models import Project
from datetime import datetime

projects = json.load(open('api/seed/projects.json'))
Project.objects.all().delete()
for project in projects:
    Project(
        project_name=project['project_name'],
        category=project['category'],
        affiliated_agency=project['affiliated_agency'],
        description=project['description'],
        project_start_time=datetime.strptime(project['project_start_time'], "%Y-%m-%d"),
        project_completion_time=datetime.strptime(project['project_completion_time'], "%Y-%m-%d"),
        total_budget=project['total_budget'],
        completion_percentage=project['completion_percentage'],
        location_coordinates=project['location_coordinates'],
    ).save()
