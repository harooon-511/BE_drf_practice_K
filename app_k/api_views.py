from app_k.serializers import *
from app_k.models import *
from rest_framework import viewsets, filters
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
   

class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = MyTokenObtainPairSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        self.http_method_names.append("GET")

        serializer = MyTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

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

    

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
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