from django.db import models

# Create your models here.

class Profile(models.Model):
    image = models.URLField(max_length=255)
    username = models.CharField(max_length=200)
    description = models.TextField()
    contact = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=255)
    link = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ManyToManyField(Profile)
    def __str__(self):
        return self.title

class Votes(models.Model):
    design= models.IntegerField(default=0)
    usability= models.IntegerField(default=0)
    content = models.IntegerField(default=0)

    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True, blank=True)

class Login(models.Model):
    username =  models.CharField(max_length=255)
    password =  models.CharField(max_length=30)








