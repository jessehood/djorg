from rest_framework import serializers, viewsets
from .models import Note

# Serializers define the API representation
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self._context['request'].user
        note = Note.objects.create(user=user, **validated_data)
        return note

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
