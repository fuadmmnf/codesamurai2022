from django.http import JsonResponse
from api.models import *
from django.forms.models import model_to_dict
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
import json
from api.dyanamic_reporter.observer import resync_db
import bcrypt


@csrf_exempt
def get_all_or_save_projects(request):
    if request.method == 'GET':
        return JsonResponse({'data': list(Project.objects.filter(is_accepted=True).filter(is_deleted=False).values())})
    if request.method in ['POST', 'PUT']:
        body = json.loads(request.body)
        print(body.get('project_id'))
        transaction = Project.objects.get(
            project_id__exact=body.get('project_id')) if request.method == 'PUT' else Project()
        transaction.project_id = body.get('project_id')
        transaction.exec = Agency.objects.get(code=body.get('exec'))
        transaction.project_name = body.get('project_name')
        transaction.location = body.get('location')
        transaction.start_date = datetime.datetime.strptime(body.get('start_date'), "%Y-%m-%d")
        transaction.latitude = body.get('latitude')
        transaction.longitude = body.get('longitude')
        transaction.cost = body.get('cost')
        transaction.timespan = body.get('timespan')
        transaction.goal = body.get('goal')
        transaction.completion = body.get('completion', None)
        transaction.rating = body.get('rating', None)
        transaction.feedback = body.get('feedback', '')
        transaction.actual_cost = body.get('actual_cost')
        transaction.is_deleted = body.get('is_deleted', False)

        transaction.save()
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
        transaction = Project.objects.get(
            project_id__exact=body.get('project_id')) if request.method == 'PUT' else Project()
        transaction.project_id = body.get('project_id')
        transaction.exec = Agency.objects.get(code__exact=body.get('exec'))
        transaction.project_name = body.get('name')
        transaction.location = body.get('location')
        transaction.latitude = body.get('latitude')
        transaction.longitude = body.get('longitude')
        transaction.cost = body.get('cost')
        transaction.timespan = body.get('timespan')
        transaction.goal = body.get('goal')
        transaction.completion = body.get('completion', None)
        transaction.is_accepted = body.get('is_accepted', False)
        transaction.proposal_date = None if not body.get('proposal_date') else datetime.datetime.strptime(
            body.get('proposal_date'), "%Y-%m-%d")

        transaction.save()
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
        transaction = Component.objects.get(
            component_id__exact=body.get('component_id')) if request.method == 'PUT' else Component()
        transaction.component_id = body.get('component_id')
        transaction.project_id = project
        transaction.executing_agency = Agency.objects.get(code__exact=body.get('execution_agency'))
        transaction.component_type = body.get('component_type'),
        transaction.depends_on = None if not body.get('depends_on') else Component.objects.get(
            component_id__exact=body.get('depends_on'))
        transaction.budget_ratio = body.get('budget_ratio')

        transaction.save()

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


def get_all_contraints(request):
    return JsonResponse({'data': list(Constraint.objects.all().values())})


def calculate_estimate_timeline(request):
    resync_db()
    return JsonResponse({'data': 'resync complete'})
