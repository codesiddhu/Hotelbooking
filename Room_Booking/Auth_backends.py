from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponse
from typing import Any
class EmailBakend(ModelBackend):
    def authenticate(self, request, username = ..., password = ..., **kwargs):
        # return super().authenticate(request, username, password, **kwargs)
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email = username)
        except UserModel.DoesNotExist:
            return None
        else:
            if username.check_password(password):
                return user
            return None
    