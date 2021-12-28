# Django
from django.urls import path

# Local Models
from task import views

urlpatterns = [
    path('', views.TaskAPiView.as_view()),
    #path('<id:pk>', views.TaskApiViewDetail.as_view()),
]