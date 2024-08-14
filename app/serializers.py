from rest_framework import serializers
from .models import CohortInfo

class CohortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CohortInfo
        fields = '__all__'
