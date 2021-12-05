from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.response import Response
from journal.models import Journal, GratitudeNote
from . import serializers

class GratitudeNoteViewset(viewsets.ModelViewSet):
    queryset = GratitudeNote.objects.all()
    serializer_class = serializers.GratitudeNoteSerializer

