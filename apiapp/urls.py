from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.TaskApi.as_view()),
    path('update-task/<int:pk>/', views.UpdateTaskApi.as_view()),
]