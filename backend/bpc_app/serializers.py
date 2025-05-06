from rest_framework import serializers
from .models import BPCRegistro

class BPCRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = BPCRegistro
        fields = '__all__'
