from django.http import JsonResponse
from api.models import Project


def index(request):
    return JsonResponse({'data': list(Project.objects.values())})
