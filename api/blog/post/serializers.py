from rest_framework import serializers

from blog import models


class BlogPostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        fields = ['title', 'text', 'image', 'user', 'date', 'id']
        model = models.BlogPost
