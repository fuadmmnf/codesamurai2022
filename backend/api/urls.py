from django.urls import path

from . import views

urlpatterns = [
    path('projects', views.get_all_or_save_projects),
    path('projects/<str:project_id>', views.get_project_detail_or_delete_by_id),
    path('proposals', views.get_all_or_save_proposals),
    path('proposals/<str:proposal_id>', views.get_proposal_detail_or_delete_by_id),
    # path('projects/filter', views.get_filtered_projects),

    path('projects/<str:project_id>/components', views.get_all_or_save_components),
    path('projects/<str:project_id>/components/<str:component_id>', views.get_component_detail_or_delete_by_id),
    path('login', views.login),
    path('agencies', views.get_all_agencies),
    path('constraints', views.get_all_contraints),
    path('estimate_timeline', views.calculate_estimate_timeline)
]
