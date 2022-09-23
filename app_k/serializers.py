from wsgiref import validate
from .models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#トークンを発行するためのクラス
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

  @classmethod
  def get_token(cls, user):
      token = super(MyTokenObtainPairSerializer, cls).get_token(user)

      # Add custom claims
      return token

class CustomUserSerializer(serializers.ModelSerializer):
  def create(self, validated_data):
    if 'password' in validated_data:
      validated_data['password'] = make_password(validated_data.get('password'))
      
    return super().create(validated_data)
    
  def update(self, instance, validated_data):
    print(validated_data['password'])
    if 'password' in validated_data:
      validated_data['password'] = make_password(validated_data.get('password'))
      
    return super().update(instance, validated_data)
    
  class Meta:
    model = CustomUser
    fields = ('id','email', 'password', 'nickname', 'username', 'date_joined', 'is_staff','is_active','is_admin')

        
    

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id','created_by', 'content', 'created_at')


class NotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = NotificationModel
    fields = ('post',)
    
class FriendlistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Friendlist
    fields = ('id','reader', 'receiver', 'read_at')