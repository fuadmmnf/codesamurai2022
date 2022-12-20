from django.http import JsonResponse
from api.models import *
from django.forms.models import model_to_dict
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
import json
import bcrypt


@csrf_exempt
def get_all_or_save_projects(request):
    if request.method == 'GET':
        return JsonResponse({'data': list(Project.objects.filter(is_accepted=True).filter(is_deleted=False).values())})
    if request.method in ['POST', 'PUT']:
        body = json.loads(request.body)
        print(body.get('project_id'))
        Project.objects.update_or_create(
            project_id=body.get('project_id'),
            exec=Agency.objects.get(code=body.get('exec')),
            project_name=body.get('project_name'),
            location=body.get('location'),
            start_date=None if not body.get('proposal_date') else datetime.datetime.strptime(
                body.get('start_date'), "%Y-%m-%d"),
            latitude=body.get('latitude'),
            longitude=body.get('longitude'),
            cost=body.get('cost'),
            timespan=body.get('timespan'),
            goal=body.get('goal'),
            completion=body.get('completion', None),
            rating=body.get('rating', None),
            feedback=body.get('feedback', ''),
            actual_cost=body.get('actual_cost'),
            is_deleted=body.get('is_deleted', False)
        )
        return JsonResponse({'data': 'updated'}, status=200)


@csrf_exempt
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
@csrf_exempt
def get_all_or_save_proposals(request):
    if request.method == 'GET':
        return JsonResponse({'data': list(Project.objects.filter(is_accepted=False).values())})
    if request.method in ['POST', 'PUT']:
        body = json.loads(request.body)
        Project.objects.update_or_create(
            project_id=body.get('project_id'),
            exec=Agency.objects.get(code__exact=body.get('exec')),
            project_name=body.get('name'),
            location=body.get('location'),
            latitude=body.get('latitude'),
            longitude=body.get('longitude'),
            cost=body.get('cost'),
            timespan=body.get('timespan'),
            goal=body.get('goal'),
            completion=body.get('completion', None),
            is_accepted=body.get('is_accepted', False),
            proposal_date=None if not body.get('proposal_date') else datetime.datetime.strptime(
                body.get('proposal_date'), "%Y-%m-%d"),
        )
        return JsonResponse({'data': 'updated'}, status=200)


@csrf_exempt
def get_proposal_detail_or_delete_by_id(request, proposal_id):
    if request.method == 'GET':
        return JsonResponse(
            {'data': model_to_dict(Project.objects.filter(is_accepted=False).get(project_id__exact=proposal_id))})
    Project.objects.filter(is_accepted=False).get(project_id__exact=proposal_id).delete()
    return JsonResponse({'data': 'successful'}, status=200)


@csrf_exempt
def get_all_or_save_components(request, project_id):
    project = Project.objects.get(project_id__exact=project_id)
    if request.method == 'GET':
        return JsonResponse({'data': list(Component.objects.filter(project_id=project).values())})
    if request.method in ['POST', 'PUT']:
        body = json.loads(request.body)
        Component.objects.update_or_create(
            component_id=body.get('component_id'),
            project_id=project,
            executing_agency=Agency.objects.get(code__exact=body.get('execution_agency')),
            component_type=body.get('component_type'),
            depends_on=None if not body.get('depends_on') else Component.objects.get(
                component_id__exact=body.get('depends_on')),
            budget_ratio=body.get('budget_ratio'),
        )
        return JsonResponse({'data': 'updated'}, status=200)


@csrf_exempt
def get_component_detail_or_delete_by_id(request, project_id, component_id):
    project = Project.objects.get(project_id__exact=project_id)

    if request.method == 'GET':
        return JsonResponse(
            {'data': model_to_dict(Component.objects.filter(project_id=project).get(component_id__exact=component_id))})
    Component.objects.get(component_id__exact=component_id).delete()
    return JsonResponse({'data': 'successful'}, status=200)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user = User.objects.prefetch_related('user_type').filter(username__exact=body.get('username')).get(
            password__exact=body.get('password').encode('utf-8'))
        if user:

            return JsonResponse({'data': {'user': model_to_dict(user), 'role': model_to_dict(user.user_type)}})
        else:
            return JsonResponse({'data': 'unauthorized'}, status=401)


@csrf_exempt
def get_all_agencies(request):
    return JsonResponse({'data': list(Agency.objects.all().values())})
