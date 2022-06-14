from rest_framework import serializers
from .models import *
class Profileserializers(serializers.Modelserializers):
    class Meta:
        model = Profile
        fields = ['image','bio','contact']
        
        
class ProjectForm(serializers.Modelserializers):
     class Meta:
        model = Project
        fields = ('title','description','project_link','image')