from rest_framework import serializers
#from .models import User
from django.contrib.auth.models import User
from mattersmithapp.models import *


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','password','first_name','last_name','email')
"""
class UserRolesSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserRoles
		fields = '__all__'
"""

