from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]
