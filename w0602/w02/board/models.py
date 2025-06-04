from django.db import models

class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100) # writer's id 
    btitle = models.CharField(max_length=100) # title
    bcontent = models.TextField() # content
    
    bgroup = models.IntegerField(default=0) # group of replies of a single post
    bstep = models.IntegerField(default=0) # sequence of the replies
    bindent = models.IntegerField(default=0) # indentation before a reply
    
    bhit = models.IntegerField(default=0) # number of views
    bfile = models.CharField(max_length=100,null=True,blank=True) 
    bdate = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return f"{self.bno}, {self.id}, {self.btitle}"
    
    
