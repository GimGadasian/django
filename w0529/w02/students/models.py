from django.db import models

class Student(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    agee = models.IntegerField(default=0)
    gender = models.CharField(max_length=30)
    sdate = models.DateTimeField(auto_now=True) 
    memo = models.TextField(blank=True) 
    
    def __str__(self):
        return f"{self.no}, {self.name}, {self.sdate}"
        
    
    
