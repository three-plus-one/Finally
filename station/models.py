from django.db import models
from login.models import Users


class Cs(models.Model):
    csId = models.IntegerField(primary_key=True)
    csAdd = models.CharField(max_length=50)
    csStates = models.BooleanField()
    csFreeTime = models.TimeField(auto_now=True)

    def __str__(self):
        return self.csAdd+self.csId.__str__()+'号'


class UserCs(models.Model):
    userTel = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    csId = models.ForeignKey(Cs, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.userTel.__str__() + '关注了'+self.csId.__str__()+'充电桩'
