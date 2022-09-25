from urllib import request
from app_k.serializers import *
from app_k.models import *
from rest_framework import viewsets, filters, status
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# firebase
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice

import json


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'date_joined',)
    ordering = ('date_joined',)
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        users = CustomUser.objects.all()

        serializer = CustomUserSerializer(users, many=True, context={"request": request})
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id','created_at',)
    ordering = ('created_at',)
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        serializer = PostSerializer(data=request.data)
        print("serialize")
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = NotificationModel.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id','post',)
    ordering = ('post',)
    permission_classes = [IsAuthenticated]
    

class FriendlistViewSet(viewsets.ModelViewSet):
    queryset = Friendlist.objects.all()
    serializer_class = FriendlistSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'read_at',)
    ordering = ('read_at',)
    permission_classes = [IsAuthenticated]

class PostReceiverViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def create(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            FCMDevice.send_topic_message(
            Message(
                notification=Notification(title="新規投稿", body="新規投稿が作成されました"),
            ),
            # Message(
            # data={
            #     "Nick" : "Mario",
            #     "body" : "great match!",
            #     "Room" : "PortugalVSDenmark"
            # },
            # topic="Optional topic parameter: Whatever you want",
            # )
            "PostCreated"
            )
            print("create")
           
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        queryset = Post.objects.all().filter(id=json.loads(request.body)['id'])
        print(json.loads(request.body)['id'])
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class UserReceiverViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class FriendlistReceiverViewSet(viewsets.ModelViewSet):
    queryset = Friendlist.objects.all()
    serializer_class = FriendlistSerializer
    permission_classes = [IsAuthenticated]
    
    


    