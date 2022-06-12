from django.shortcuts import render,redirect
from .models import Project
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="index.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))  


def index(request):
    '''
    get all the images from the database and order them by the date they were created
    '''
    projects = Project.objects.all()
    return render(request, 'index.html', {'project': projects})

@login_required(login_url='accounts/login')
def project_detail(request):
    # template_name = 'project_detail.html'
    if request.method == 'POST':
        project_form = ProjectForm(data=request.POST)
        if project_form.is_valid():
            project_form.save()
            # return redirect('index')
    else:
        project_form = ProjectForm()
		# new_project='new_prpoject'
    return render(request,'project_detail.html', { 'project_form': project_form})

def display_project(request):
    
    if request.method =="GET":
        project=Project.objects.all();
        # absolute_url=request.build_absolute_uri()
        return render(request,'project_detail.html',{'all_project':project})

@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = NewUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = NewUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }


    return render(request, 'profile.html' )