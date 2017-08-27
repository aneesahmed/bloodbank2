# coding=utf-8
from rest_framework import serializers
from patient.models import Bloodgroup

class BloodgroupSerializer(serializers.ModelSerializer):
    """
    Serializing all the 
    """
    class Meta:
        model = Bloodgroup
        fields = ('bloodgroupId', 'bloodgroupDetails', 'bloodgroupType')