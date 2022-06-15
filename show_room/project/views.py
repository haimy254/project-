
from django.shortcuts import render,redirect
from .models import Project
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, ProjectForm, ProfileForm, ReviewForm
from django.views.decorators.csrf import csrf_exempt
from .serializers import Profileserializers,Projectserializers
from .models import Profile,Project, Review


from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"register_form":form})

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
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))  


def home(request):
    return render(request, template_name="home.html")

@login_required
@transaction.atomic
def save_project(request):
    request.user.id = request.user
    if request.method == 'POST':
        project_form = ProjectForm(data=request.POST)
       
        if project_form.is_valid(): 
            
            obj=project_form.save(commit=False)
            obj.profile_id=request.user.id
            obj.save()
            return HttpResponseRedirect('home')
    else:
        project_form = ProjectForm()
		# new_project='new_prpoject'
    return render(request,'project_detail.html', { 'project_form': project_form})

@login_required
def display_projects(request,):
    # get all projects from db
    project=Project.objects.all();
    reviews = Review.objects.all()
    
    return render(request,'project_detail.html',{'all_project':project,'review':reviews})

def rev(request, project):
    project = Project.objects.get(title=project)
    print (request.user)
    print(project)
    reviews =Review.objects.filter(user=request.user, project=project).first()
    print(reviews)
    
    if request.method == 'POST':
        # project= Project.objects.filter_by(pk=id)/
        review_form = ReviewForm(data=request.POST)
        
        
        if review_form.is_valid():
            
            review=review_form.save(commit=False)
            review.user=request.user
            # review.project=project
            review.save()
            # messages.success(request, 'Your profile is updated successfully')
            return redirect(home)
    else:
        review_form = ReviewForm()
    
    return render(request,'project_detail.html',locals())

@login_required
@transaction.atomic
def save_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            Profile.objects.get_or_create(user=request.user)
            profile_form.save()
            
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        profile_form = ProfileForm()
        
    context = {
        'profile_form': profile_form
    }
    
    return render(request, 'profile.html',context )

@transaction.atomic
def profile_view(request):
    if request.method=="GET":
        profile=Profile.objects.filter(user=request.user);
        project = Project.objects.filter(user=request.user);
    return render(request,'profile_view.html',{'profile':profile,'project':project})

@login_required
@transaction.atomic
def review(request):
    if request.method == 'POST':
        # project= Project.objects.filter_by(pk=id)/
        review_form = ReviewForm(data=request.POST)
        
        
        if review_form.is_valid():
            
            review=review_form.save(commit=False)
            review.user=request.user
            # review.project=project
            review.save()
            # messages.success(request, 'Your profile is updated successfully')
            return redirect(home)
    else:
        review_form = ReviewForm()
        # project= Project
    return render(request,'review.html', { 'review_form': review_form})
@transaction.atomic
def display_review(request):
    
    if request.method=="GET":
        review=Review.objects.all();
        # project = Project.objects.all(pk=id);
        
    return render(request,'profile_detail.html',{'reviews':review})


@csrf_exempt
def search(request):   
    if request.method=='POST':
        search_term = request.POST.get("title")
       
       
       
        project_found_by_image=Project.objects.get(title=search_term)
        
        if project_found_by_image:
            found_projects=project_found_by_image
            print(found_projects)
            message = f"{search_term}" 
            
            return render(request, 'search.html',{"message":message,"projects": found_projects})  
        else:
            message="no such resource found"
            projects=Project.objects.all()
            return render(request,'project_detail.html',{"message":message,'project':projects})
              
    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})    
    
    
@api_view(["GET"])
def api_profile(request):
    profile= Profile.objects.all()
    serializer = Profileserializers(profile,many=True)
    
    return Response(serializer.data)

@api_view(["GET"])
def api_project(request):
    profile= Project.objects.all()
    serializer = Projectserializers(profile,many=True)
    
    return Response(serializer.data)

