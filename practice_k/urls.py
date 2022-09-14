from django.urls import path, include
from rest_framework import routers
from app_k import api_views as app_k_api_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from app_k.views import *


router = routers.DefaultRouter()
router.register('customusers', app_k_api_views.CustomUserViewSet)
router.register('posts', app_k_api_views.PostViewSet)
router.register('notifications', app_k_api_views.NotificationViewSet)
router.register('friendlists', app_k_api_views.FriendlistViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
