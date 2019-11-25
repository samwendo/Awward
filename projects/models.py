from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 30,null = True)
    description = models.TextField(null = True)
    link = models.CharField(max_length = 70,null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images 

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    def __str__(self):
    	return self.user.username
    
    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains = search_term)
        return project
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = HTMLField()
    profile_pic = models.ImageField(upload_to='images/')
    contact_info= models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

class Rating(models.Model):
    rating= models.CharField(max_length=30, null=True)
    

    def __str__(self):
        return self.rating


    def delete_rating(self):
        self.delete()

    def save_rating(self):
        self.save()
