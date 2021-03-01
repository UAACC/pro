from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import PostsViewSet

router = routers.DefaultRouter()
router.register('post',PostsViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
