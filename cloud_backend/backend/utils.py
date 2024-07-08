from .models import *


def exist_username(username):
    return User.objects.filter(username=username).exists()
