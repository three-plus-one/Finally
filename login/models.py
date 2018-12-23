from django.db import models
from datetime import datetime


class Users(models.Model):
    userTel = models.CharField(primary_key=True, max_length=12)
    userName = models.CharField(max_length=16, default='朱老师')
    userMail = models.CharField(max_length=20, null=True)
    userPwd = models.CharField(max_length=20)

    def __str__(self):
        return self.userName


