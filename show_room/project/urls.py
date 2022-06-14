from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('',register_request, name="register"),
    path('home/',home,name= 'home'),
    path('save_project/',save_project,name='save_project'),
    
    path('logout/',user_logout,name='user_logout'),
    path('login/',login_request,name="login"),
     path('profile/',save_profile, name='user_profile'),
     
    path('project_detail/',display_projects,name="project_detail"),
    path('profile_view/',profile_view,name="profile"),
    
    path('review/',review,name= 'review'),
    path('api/',api_view, name="api")
]


if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)