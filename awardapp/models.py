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
    RATING_CHOICES = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
    )
    design=models.IntegerField(choices=RATING_CHOICES,blank=True,null=True)
    usability=models.IntegerField(choices=RATING_CHOICES,blank=True,null=True)
    content= models.IntegerField(choices=RATING_CHOICES,blank=True,null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='profile',null=True,blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True, blank=True)

    def save_review(self):
        self.save()
    def delete_review(self):
        self.delete()
    def __str__(self):
        return self.profile.username


     
   
class Login(models.Model):
    username =  models.CharField(max_length=255)
    password =  models.CharField(max_length=30)








