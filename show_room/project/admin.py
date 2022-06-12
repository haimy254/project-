from django.contrib import admin
from .models import Project,Review,Profile
# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Review)

