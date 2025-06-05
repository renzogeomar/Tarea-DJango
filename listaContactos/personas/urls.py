from django.urls import path
from . import views

urlpatterns = [
    path('descripcion/', views.descripcion, name='descripcion'),
]