from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from blog import models
from blog.post import serializers


class PostView(ListCreateAPIView):
    serializer_class = serializers.BlogPostSerializer
    model = models.BlogPost
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.model.objects.all().order_by('-date')

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class SinglePostView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = serializers.BlogPostSerializer
    model = models.BlogPost

    def get_queryset(self):
        return self.model.objects.all().order_by('-date')
