from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, BlogViewSet


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'blog', BlogViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
