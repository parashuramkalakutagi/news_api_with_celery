from .models import *
from rest_framework import serializers

class BusinessNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBusiness
        fields = '__all__'


class journalSerializer(serializers.ModelSerializer):
    class Meta:
        model = journal
        fields = '__all__'
