from django.shortcuts import render

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import json
from django.http import HttpResponse
import uuid
from TodoApi import models


# Create your views here.
# def sign up



def register(request):
	# get username and password
	data = json.loads(request.body.decode(),'utf-8')
	username= data['username']
	password= data['password']
	# assign a token
	token = uuid.uuid4().hex
	# print()
	# check if username exists
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		user = User.objects.create_user(username, password)
		user.save()

	# user_list = models.User.object.filter(username=username)
	# if len(user_list) == 0:
	# 	user = models.User.objects.create(username=username,password=password)
	# # else: username taken
		# Create user
	# else save user to db
		#TODO connect user to progile
	# build some dictionary with verifications message and token
	context={
		'token':token,
		'msg': 'you successfully reg'
	}

	return JsonResponse(context)
	# send back some json response

def login(request):
	#load data 
	data = json.loads(request.body.decode(),'utf-8')
	username= data['username']
	password= data['password']
	
	try:
		#get username
		user = authenticate(username=username,password=password)
		#if password matches that of our data
		if user is not None:
			#create a user session
			if user.is_active:
				login(request,user)
				#dictionary to return they logged in
				context={
				"logged":"you are now logged in"
				}
				
				return JsonResponse(context)

			else:
				return HttpResponse("account disables.")
		else:
			return HttpResponse("Invalid login details supplied.")

	except User.DoesNotExist:

		context = {
		"notlogged":"username/password does not match"
		}

		return JsonResponse(context)


def logout(request):
	logout(request)
	context = {
		"logged out":"you have been logged out"
		}

	return JsonResponse(context)


def create(request):
	data = json.loads(request.body.decode())
	print(data)






