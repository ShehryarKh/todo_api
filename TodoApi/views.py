from django.shortcuts import render

from django.http import JsonResponse
from django.contrib.auth.models import User

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
		data = json.loads(request.body.decode(),'utf-8')

	
	try:
		user = User.objects.get(username=data['username'])
		if user.password== request.POST['password']:
			request.session['user_id'] =user_id




