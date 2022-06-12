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
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        profile_pic= models.ImageField(default='default.jpg', upload_to='profile_pics')
        bio = models.CharField(max_length=200)
        contact = models.IntegerField()
        
        
        # def __str__(self):
        #     return f'{self.user.username} Profile'
        
        # def save(self):
        #     # super().save()

        #     profile_pic = Project.open(Self.user.path) # Open image
        
        # # resize image
        #     if profile_pic.height > 300 or profile_pic.width > 300:
        #         output_size = (300, 300)
        #         profile_pic.thumbnail(output_size) # Resize image
        #         profile_pic.save(Self.projects.path)