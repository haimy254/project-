from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class Loginform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
        


class ProjectForm(forms.ModelForm):
     class Meta:
        model = Project
        fields = ['title', 'description', 'project_link','image']
        
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','contact']
        

def form_validation_error(form):
    """
    Form Validation Error
    If any error happened in your form, this function returns the error message.
    """
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg

class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = ('rating','review')
