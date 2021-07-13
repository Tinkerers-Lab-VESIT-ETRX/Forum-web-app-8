from django.db import models 
from django.contrib.auth.models import User

class forum(models.Model):
    name=models.CharField(max_length=100,default="anonymous" )
    email=models.CharField(max_length=100,null=True)
    topic= models.CharField(max_length=500)
    description = models.CharField(max_length=100000,blank=True)
    link = models.CharField(max_length=300 ,null =True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    image = models.ImageField(upload_to='images/') 

    def __str__(self):
        return str(self.topic)

class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=100000)
    image = models.ImageField(upload_to='discussion_images/') 
    
    def __str__(self):
        return str(self.forum)
