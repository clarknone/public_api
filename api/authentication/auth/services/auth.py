from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

UserModel = get_user_model()

Error = str


# def create_user(username: str, password: str) -> UserModel | bool:
def create_user(username, password):
    try:
        user = UserModel.objects.create_user(username, password=password)
        return user
    except IntegrityError:
        return False


# def validate_user(username: str, password: str) -> UserModel | Error:
def validate_user(username, password):
    """ Validate user """
    # error: Error = ''
    error = ''
    try:
        user: UserModel = UserModel.objects.get(username=username.lower())
        if user.check_password(password):
            return user
        error = "incorrect password"
    except UserModel.DoesNotExist:
        """ Auto create users for now """
        # error = "User does not exist"

        user = create_user(username, password)
        return user
    if error:
        raise ValidationError(detail=error)
