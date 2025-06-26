from django.urls import path
from . import views
from .views import (
    PersonaListView,
    PersonaDetailView,
    PersonaCreateView,
    PersonaUpdateView,
    PersonaDeleteView,
)

urlpatterns = [
    #path('descripcion/', views.descripcion, name='descripcion'),
    path('', PersonaListView.as_view(), name='persona-list'),
    path('<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
    path('create/', PersonaCreateView.as_view(), name='persona-create'),
    path('update/<int:pk>/', PersonaUpdateView.as_view(), name='persona-update'),
    path('delete/<int:pk>/', PersonaDeleteView.as_view(), name='persona-delete'),
]