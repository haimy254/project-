from rest_framework import serializers
from .models import *
class Profileserializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image','bio','contact','user']
        
        
class Projectserializers(serializers.ModelSerializer):
     class Meta:
        model = Project
        fields = ('title','description','project_link','image')