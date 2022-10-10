from django.contrib.auth import get_user_model
from django.utils.timezone import now
from rest_framework.authtoken.models import Token


def login_helper(data: dict, user: get_user_model()) -> dict:
    if user:
        user.last_login = now()
        user.save()
        token, _ = Token.objects.get_or_create(user=user)
        token.delete()
        token = Token.objects.create(user=user)
        data['token'] = token.key
        data['type'] = user.type
    return data
