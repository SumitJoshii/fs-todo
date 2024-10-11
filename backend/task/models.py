from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend    

# Create your models here.
#-----------------Not using custom USER----------------------
# class User(models.Model):
#     first_name = models.CharField(max_length=30, null=False)
#     last_name = models.CharField(max_length=30, null=False)
#     email = models.EmailField(null=False, unique=True)
#     password = models.CharField(max_length=30, null=False)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    list_name = models.CharField(max_length=50, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_important = models.BooleanField(default=False)

class MyTask(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        print("Ye bhi BKL hai")
        try:
            print(email)
            print(username)
            email = email if email else username
            user = UserModel.objects.get(email=email)
            # if email:
            #     user = UserModel.objects.get(email=email)
            # else:
            #     user = UserModel.objects.get(username=username)
            print(user)
        except UserModel.DoesNotExist:
            
            print("Itta bada BKL bhai sahab")

            try:
                user = UserModel.objects.get(username=email)
            
            except UserModel.DoesNotExist:
                print("Saale Bhak, BKL!")
                return None
            else:
                print("Upar")
                if user.check_password(password):
                    print("Neeche")
                    return user
            return None
        else:
            print("Upar")
            if user.check_password(password):
                print("Neeche")
                return user
        return None


# Django inbuild user and Login function
# Poora backend complete
# Simple user api, List and Task API

# [1,2,3,4] A -1 + 2 = 1 A
# [2,4,1,0] B 1 + (-2) = -1
# e/o = e

# --------------
# Django Template - Html
# ChatGPT maxx
