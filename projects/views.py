from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Project, Profile
from django.contrib.auth.models import User
from .form import NewProjectForm, ProfileForm, RatingForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def projects_today(request):
    all_images= Project.objects.all()
    print(all_images)
    profile = Profile.objects.all()
    form = RatingForm()
    return render(request, 'all-projects/today-project.html', { "images":all_images,"profiles":profile,  "form":form})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_images = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"message":message})        



@login_required(login_url='/accounts/login/')
def new_project(request):
    
        current_user = request.user
        title = 'New project'
        if request.method == 'POST':
            form = NewProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = current_user
                project.save()
            return redirect('projectsToday')

        else:
            form = NewProjectForm()
        return render(request, 'new_project.html', {"form": form,"current_user":current_user,"title":title})

@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
   
    return render(request,'profile.html',{"user":user, "profiles":profiles})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('projectsToday')

    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {"form": form})

@login_required(login_url='/accounts/login/')
def rating(request,id):
    current_user = request.user
    users = User.objects.get(pk=current_user.id)
    projects = Project.objects.get(pk=id)
    print(users)
    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = users
            rating.project=projects
            rating.save()
        return redirect('projectsToday')
    else:
        return redirect('projectsToday')