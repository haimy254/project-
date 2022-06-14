from rest_framework import serializers
from .models import *
class Profileserializers(serializers.Modelserializers):
    class Meta:
        model = Profile
        fields = ['image','bio','contact']
        
        
