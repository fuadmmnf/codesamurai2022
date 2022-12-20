from django.http import JsonResponse
from api.models import *
from django.forms.models import model_to_dict
import datetime


def get_all_or_save_projects(request):
    if request.method == 'GET':
        return JsonResponse({'data': list(Project.objects.filter(is_accepted=True).filter(is_deleted=False).values())})
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
            actual_cost=request.POST.get('actual_cost'),
            is_deleted=request.POST.get('is_deleted', False)
        )
        return JsonResponse({'data': 'updated'}, status=200)


def get_project_detail_or_delete_by_id(request, project_id):
    if request.method == 'GET':
        return JsonResponse({'data': model_to_dict(
            Project.objects.filter(is_accepted=True).filter(is_deleted=False).get(project_id=project_id))})
    Project.objects.filter(is_accepted=True).get(project_id__exact=project_id).delete()
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

def get_all_or_save_proposals(request):
    if request.method == 'GET':
        return JsonResponse({'data': list(Project.objects.filter(is_accepted=False).values())})
    if request.method in ['POST', 'PUT']:
        Project.objects.update_or_create(
            project_id=request.POST.get('project_id'),
            exec=Agency.objects.get(code__exact=request.POST.get('exec')),
            project_name=request.POST.get('name'),
            location=request.POST.get('location'),
            latitude=request.POST.get('latitude'),
            longitude=request.POST.get('longitude'),
            cost=request.POST.get('cost'),
            timespan=request.POST.get('timespan'),
            goal=request.POST.get('goal'),
            completion=request.POST.get('completion', None),
            is_accepted=request.POST.get('is_accepted', False),
            proposal_date=None if not request.POST.get('proposal_date') else datetime.datetime.strptime(
                request.POST.get('proposal_date'), "%Y-%m-%d"),
        )
        return JsonResponse({'data': 'updated'}, status=200)


def get_proposal_detail_or_delete_by_id(request, proposal_id):
    if request.method == 'GET':
        return JsonResponse(
            {'data': model_to_dict(Project.objects.filter(is_accepted=False).get(project_id=proposal_id))})
    Project.objects.filter(is_accepted=False).get(project_id__exact=proposal_id).delete()
    return JsonResponse({'data': 'successful'}, status=200)


def get_all_or_save_components(request, project_id):
    project = Project.objects.get(project_id__exact=project_id)
    if request.method == 'GET':
        return JsonResponse({'data': list(Component.objects.filter(project_id=project).values())})
    if request.method in ['POST', 'PUT']:
        Component.objects.update_or_create(
            component_id=request.POST.get('component_id'),
            project_id=project,
            executing_agency=Agency.objects.get(code__exact=request.POST.get('execution_agency')),
            component_type=request.POST.get('component_type'),
            depends_on=None if not request.POST.get('depends_on') else Component.objects.get(
                component_id__exact=request.POST.get('depends_on')),
            budget_ratio=request.POST.get('budget_ratio'),
        )
        return JsonResponse({'data': 'updated'}, status=200)


def get_component_detail_or_delete_by_id(request, project_id, component_id):
    project = Project.objects.get(project_id__exact=project_id)

    if request.method == 'GET':
        return JsonResponse(
            {'data': model_to_dict(Component.objects.filter(project_id=project).get(component_id__exact=component_id))})
    Component.objects.get(component_id__exact=component_id).delete()
    return JsonResponse({'data': 'successful'}, status=200)
