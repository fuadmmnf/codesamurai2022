from django.http import JsonResponse
from api.models import Project
from django.forms.models import model_to_dict
import datetime

def get_all_projects(request):
    return JsonResponse({'data': list(Project.objects.values())})

def get_project_detail_by_id(request, project_id):
    return JsonResponse({'data': model_to_dict(Project.objects.get(id=project_id))})


def get_filtered_projects(request):
    category = request.GET.get('category', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    filtered_projects = Project.objects
    if category is not None:
        filtered_projects = filtered_projects.filter(category__exact=category)
    if start_date is not None:
        filtered_projects = filtered_projects.filter(project_start_time__lte=datetime.datetime.strptime(start_date, "%Y-%m-%d"),)
    if end_date is not None:
        filtered_projects = filtered_projects.filter(project_completion_time__gte=datetime.datetime.strptime(end_date, "%Y-%m-%d"),)
    return JsonResponse({'data': list(filtered_projects.values())})
