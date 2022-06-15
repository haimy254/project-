from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.profile = Profile( image='image.jpg', bio='lovely',contact='07897654')
        
    def test_instance(self):
        pass