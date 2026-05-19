from django.urls import path
from . import views

app_name = 'incidents'

urlpatterns = [
    # Cambiamos views.home por views.IncidentListView.as_view()
    path('', views.IncidentListView.as_view(), name='home'),
    path('create/', views.IncidentCreateView.as_view(), name='create'),
    path('<int:pk>/', views.IncidentDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.IncidentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.IncidentDeleteView.as_view(), name='delete'),
]