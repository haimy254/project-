from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.profile = Profile( image='image.jpg', bio='lovely',contact='07897654')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    def test_save_method(self):
        self.profile.save() 
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
        
class ProjectTestClass(TestCase):
    
    def setUp(self):
        self.project = Project(image = 'image.jpg', title = 'project', description = 'text')
    
             
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))  
        
       
    