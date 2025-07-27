from rest_framework import serializers
from .models import WorkImage

class WorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkImage
        fields = '__all__'