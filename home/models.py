from platform import release
from random import choice
from django.contrib.auth import get_user_model



from django.db import models
from datetime import datetime

User=get_user_model()
# Create your models here.
class Genres(models.Model):
    name=models.CharField(max_length=100)
    genre_image=models.ImageField(upload_to='genre_images',default='blank_profile.png')
    
    
    def __str__(self):
        return self.name



class Movies(models.Model):
    title=models.CharField(max_length=100)
    genre=models.ForeignKey(Genres,on_delete=models.SET_NULL,null=True)
    director=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    lead_actor=models.CharField(max_length=100)
    release_date=models.DateField()
    movie_images=models.ImageField(upload_to='movie_images',default='blank_profile.png')
    
    
    def __str__(self):
        return self.title



class admin_login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
    def __str__(self):
        return self.username
    



class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user= models.IntegerField()
    bio=models.TextField(blank=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    
    mobile=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.fname
    



class Review(models.Model):
    description=models.TextField(help_text="write your commet")
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    comment_date=models.DateTimeField(auto_now_add=True)
    Movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    time=models.DateField(default=datetime.now)
    
    
    
class Rating(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    rate = models.IntegerField()
    
    def __str__(self):
        return self.Movie.title
    


    
class Watchlist(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.author.username
     
    
    

    

    

    
    
    
