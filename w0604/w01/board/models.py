from django.db import models

class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100)
    btitle = models.CharField(max_length=1000)
    bcontent = models.TextField()
    # 답글 달기
    bgroup = models.IntegerField(default=0) # 답글달기 묶음
    bstep = models.IntegerField(default=0) # 답글달기 순서
    bindent = models.IntegerField(default=0) # 들여쓰기
    # --------
    bhit = models.IntegerField(default=0)
    bfile = models.CharField(max_length=100, null=True, blank=True)
    bdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bno}, {self.btitle}, {self.bgroup}"