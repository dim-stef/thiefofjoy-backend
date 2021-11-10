from django.db import models
import uuid

# Create your models here.
class Journal(models.Model):
    pass


class GratitudeNote(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name="gratitude_notes")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
