from django import forms
from .models import Project,Profile,Rating

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class RatingForm(forms.ModelForm):
	class Meta:
		model = Rating
		
		exclude = ['user','profile',]
