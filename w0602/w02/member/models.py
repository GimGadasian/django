from django.db import models

class Member(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    pw = models.CharField(max_length=50)
    nick = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,default='남자')
    hobby = models.CharField(max_length=50,default='게임')
    
    def __str__(self):
        return f"{self.id}, {self.pw}, {self.nick}"
