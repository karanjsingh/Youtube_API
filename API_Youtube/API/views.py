from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .Youtube_api import getnewposts
from .models import Videos
from .serializers import VideosSerializer
from API_Youtube import settings

def save_api():
    q = settings.QUERRY
    print(q)
    getnewposts(q)

class VideoList(generics.ListAPIView):
    queryset = Videos.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # Adding the search and filter fields
    search_fields = ['title']
    filter_fields = ['channelTitle']
    ordering = ['-publishingDateTime']
    serializer_class = VideosSerializer
    pagination_class = PageNumberPagination
    