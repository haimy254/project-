from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    
    title = models.CharField(max_length=90)
    description = models.CharField(max_length=800)
    post_time = models.DateTimeField(auto_now_add=True)
    project_link = models.URLField(("project link"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
 
    class Meta:
        ordering = ['-post_time']

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

class Profile(models.Model):
    
        profile_pic= models.ImageField(default='default.jpg', upload_to='profile_pics')
        bio = models.CharField(max_length=200)
        contact = models.IntegerField()
        
        
        def __str__(self):
            return f'{self.user.username} Profile'