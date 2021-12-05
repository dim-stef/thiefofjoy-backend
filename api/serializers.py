from rest_framework import routers, serializers, viewsets
from journal.models import Journal, GratitudeNote


class GratitudeNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GratitudeNote
        fields = ['body', 'journal']
