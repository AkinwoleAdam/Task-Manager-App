from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
  user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  description = models.TextField()
  date_created = models.DateTimeField(auto_now_add = True)
  date_updated = models.DateTimeField(auto_now = True)
  completed = models.BooleanField(default=False)
  
  def __str__(self):
    return self.title
    
class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField()
  avatar = models.ImageField(default='profile1.png',null=True)
  
  def __str__(self):
    return f'{self.user.username} Profile'