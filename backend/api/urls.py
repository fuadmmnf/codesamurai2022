from django.urls import path

from . import views

urlpatterns = [
    path('projects', views.get_all_or_save_projects),
    path('projects/<str:project_id>', views.get_project_detail_or_delete_by_id),
    path('projects/filter', views.get_filtered_projects),
]