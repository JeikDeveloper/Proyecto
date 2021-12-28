# Django
from django.urls import path

# Local Models
from task.views import TaskAPiView
from task.views import TaskApiViewDetail

urlpatterns = [
    path('api', TaskAPiView.as_view()),
    path('api/<int:pk>', TaskApiViewDetail.as_view()),
]