from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from authentication import models


class LoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = models.User
        fields = ('username', 'password', 'token')
        extra_kwargs = {'password': {'write_only': True}}
