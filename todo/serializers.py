from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
 class Meta:
        model = User
        fields = [ 'username' ]

class TodoSerializer(serializers.HyperlinkedModelSerializer):
  # user = UserSerializer()
   class Meta:
        model = Todo
        fields = ['id','title', 'description', 'created_at','time_passed']

