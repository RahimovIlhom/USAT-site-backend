from rest_framework import serializers

from advantages.models import Advantage


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ('id', 'title', 'content', 'created_at')
