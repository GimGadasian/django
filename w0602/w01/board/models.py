from django.db import models

class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100)
    btitle = models.CharField(max_length=100)
    bcontent = models.TextField(max_length=1000)
    bgroup = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    bhit = models.DateField(auto_now=True)
    bdate = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.bno}, {self.id}, {self.btitle}"