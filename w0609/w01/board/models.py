from django.db import models
from member.models import Member
class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    btitle = models.CharField(max_length=1000)
    bcontent = models.TextField()
    
    bgroup = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    
    bhit = models.IntegerField(default=0)
    bfile = models.CharField(max_length=20, null=True, blank=True)
    
    notice = models.IntegerField(default=0)  # 공지사항 여부 필드 추가
    bdate = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.bno}, {self.id}, {self.btitle}, notice={self.notice}' 
