from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('index',index,name= 'index'),
    path('project/',project_detail,name='project_detail'),
    path("",register_request, name="register"),
    path('logout/',user_logout,name='user_logout'),
    path('login/',login_request,name="login"),
     path('profile/',profile, name='user_profile'),
    path('project_view/',display_project,name="project_view")
]


if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)