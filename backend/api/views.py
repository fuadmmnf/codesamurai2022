from django.http import JsonResponse
from api.models import *
from django.forms.models import model_to_dict
import datetime


def get_all_or_save_projects(request):
    if request.method == 'GET':
        return JsonResponse({'data': list(Project.objects.values())})
    if request.method in ['POST', 'PUT']:
        Project.objects.update_or_create(
            project_id=request.POST.get('project_id'),
            exec=Agency.objects.get(code__exact=request.POST.get('exec')),
            project_name=request.POST.get('name'),
            location=request.POST.get('location'),
            start_date=None if not request.POST.get('proposal_date') else datetime.datetime.strptime(
                request.POST.get('start_date'), "%Y-%m-%d"),
            latitude=request.POST.get('latitude'),
            longitude=request.POST.get('longitude'),
            cost=request.POST.get('cost'),
            timespan=request.POST.get('timespan'),
            goal=request.POST.get('goal'),
            completion=request.POST.get('completion', None),
            rating=request.POST.get('rating', None),
            feedback=request.POST.get('feedback', ''),
            is_accepted=request.POST.get('is_accepted', True),
            actual_cost=request.POST.get('actual_cost', None),
            proposal_date=None if not request.POST.get('proposal_date') else datetime.datetime.strptime(
                request.POST.get('proposal_date'), "%Y-%m-%d"),
        )
        return JsonResponse({'data': 'updated'}, status=200)


def get_project_detail_or_delete_by_id(request, project_id):
    if request.method == 'GET':
        return JsonResponse({'data': model_to_dict(Project.objects.get(id=project_id))})
    Project.objects.get(project_id__exact=project_id)
    return JsonResponse({'data': 'successful'}, status=200)

#
# def get_filtered_projects(request):
#     category = request.GET.get('category', None)
#     start_date = request.GET.get('start_date', None)
#     end_date = request.GET.get('end_date', None)
#     filtered_projects = Project.objects
#     if category is not None:
#         filtered_projects = filtered_projects.filter(category__exact=category)
#     if start_date is not None:
#         filtered_projects = filtered_projects.filter(
#             project_start_time__lte=datetime.datetime.strptime(start_date, "%Y-%m-%d"), )
#     if end_date is not None:
#         filtered_projects = filtered_projects.filter(
#             project_completion_time__gte=datetime.datetime.strptime(end_date, "%Y-%m-%d"), )
#     return JsonResponse({'data': list(filtered_projects.values())})
