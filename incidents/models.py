from django.db import models

class Incident(models.Model):
    # Opciones para el campo de severidad (Requisito del laboratorio)
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='Low')
    reported_at = models.DateTimeField(auto_now_add=True)  # Se pone sola al crear
    updated_at = models.DateTimeField(auto_now=True)      # Se actualiza sola al editar
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.title