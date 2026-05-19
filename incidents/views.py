from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Incident

# Desafío 1: Listar incidentes
class IncidentListView(ListView):
    model = Incident
    template_name = 'incidents/home.html'
    context_object_name = 'incidents'

# Desafío 2: Ver detalle del incidente
class IncidentDetailView(DetailView):
    model = Incident
    template_name = 'incidents/detail.html'

# Desafío 3: Registrar nuevo incidente
class IncidentCreateView(CreateView):
    model = Incident
    template_name = 'incidents/create.html'
    fields = ['title', 'description', 'severity', 'resolved']
    success_url = reverse_lazy('incidents:home')

# Desafío 4: Actualizar incidente existente
class IncidentUpdateView(UpdateView):
    model = Incident
    template_name = 'incidents/update.html'
    fields = ['title', 'description', 'severity', 'resolved']
    success_url = reverse_lazy('incidents:home')

# Desafío 5: Eliminar incidente
class IncidentDeleteView(DeleteView):
    model = Incident
    template_name = 'incidents/confirm_delete.html'
    success_url = reverse_lazy('incidents:home')