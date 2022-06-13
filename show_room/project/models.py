from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE,default=1,null=True)
        # profile_pic= models.ImageField(default='default.jpg', upload_to='profile_pics/')
        image = models.ImageField(default='default.jpg', upload_to='project/')
        
        bio = models.CharField(max_length=200)
        contact = models.IntegerField()
        
        def __str__(self):
            return self.user.username
        
        def save(self):
            super().save()

            img = Project(self.profile_pic.path)


    
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    image = models.ImageField(default='default.jpg', upload_to='project/')
    title = models.CharField(max_length=90)
    description = models.CharField(max_length=800)
    post_time = models.DateTimeField(auto_now_add=True)
    project_link = models.URLField(("project link"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )
    profile = models.ForeignKey(Profile,on_delete= models.CASCADE)
    review=models.ManyToManyField('Review', blank=True)
    class Meta:
        ordering = ['-post_time']

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'), 
        (10, '10'),
    )
    review = models.CharField(max_length=200)
    userbility = models.IntegerField(choices=RATING_CHOICES)
    content = models.IntegerField(choices=RATING_CHOICES)
    design = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
         
