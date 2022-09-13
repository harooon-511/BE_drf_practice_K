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
  class Meta:
    model = CustomUser
    fields = ('email', 'password', 'nickname', 'username', 'date_joined', 'is_staff', 'is_admin')

    def create(self, validated_data):
      validated_data['password'] = make_password(validated_data.get('password'))
      return super(CustomUserSerializer, self).create(validated_data)

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('created_by', 'content', 'created_at')


class NotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields = ('post',)
    
class FriendlistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Friendlist
    fields = ('reader', 'receiver', 'read_at')