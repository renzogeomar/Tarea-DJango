from django.urls import path
from . import views
from .views import (
    PersonaListView,
)

urlpatterns = [
    #path('descripcion/', views.descripcion, name='descripcion'),
    path('', PersonaListView.as_view(), name='persona-list'),
]