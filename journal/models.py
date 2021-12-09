from django.db import models
from accounts.models import User
import uuid

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="journal", null=True, blank=True)

    def __str__(self):
        return self.user.email


class GratitudeNote(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name="gratitude_notes")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StrengtheNote(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name="strength_notes")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
