from django.urls import path, include
from . import views
from .views import update_task_status,update_task_status_history

urlpatterns = [
    path("", views.Home, name="task-home"),
    path('update-task-status/', update_task_status, name='update_task_status'),
    path('update-task-status-history/', update_task_status_history, name='update_task_status_history'),
    path("task/<int:pk>/delete", views.TaskDeleteView.as_view(), name="task-delete"),
    path("task/create", views.TaskCreateView.as_view(), name="task-create"),
    path("history/", views.History, name='task-history')
]
