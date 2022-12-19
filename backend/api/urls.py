from django.urls import path

from . import views

urlpatterns = [
    path('projects', views.get_all_projects),
    path('projects/<int:project_id>', views.get_project_detail_by_id),
    path('projects/filter', views.get_filtered_projects),
]