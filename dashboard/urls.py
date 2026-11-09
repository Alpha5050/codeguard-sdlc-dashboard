from django.urls import path
from . import views

urlpatterns = [
    path('', views.finding_list, name='finding_list'),
    path('add/', views.finding_create, name='finding_create'),
    path('edit/<int:finding_id>/', views.finding_edit, name='finding_edit'),
    path('delete/<int:finding_id>/', views.finding_delete, name='finding_delete'),
]