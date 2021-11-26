from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/<str:name>', views.dashboard),
    path('', views.home),
]