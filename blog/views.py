from rest_framework import viewsets

from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'
