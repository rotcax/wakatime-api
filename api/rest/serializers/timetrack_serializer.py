from rest.imports import serializers
from rest.models.models import TimeTrack

class TimeTrackSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = TimeTrack
        fields = ['id', 'created_at', 'start', 'end', 'timezone']