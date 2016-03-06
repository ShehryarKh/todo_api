from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User)
	#add field with token
	token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)



class Todo(models.Model):
	task = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now=True, auto_now_add=False) 
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False) 
	completed = models.BooleanField(default=True)
	user = models.ForeignKey(User)

	

