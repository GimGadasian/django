from django.db import models

class Product:
   code = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   chategory_h = models.CharField(max_length=100)
   chategory_l = models.CharField(max_length=100)
   origin = models.CharField(max_length=100)
   weight = models.ImageField(default=0)
   price = models.ImageField(default=0)
   price_disc = models.ImageField(default=0)
   stock = models.ImageField(default=0)
   image_m = models.ImageField(upload_to='', null=True, blank=True)
   image_s1 = models.ImageField(upload_to='', null=True, blank=True)
   image_s2 = models.ImageField(upload_to='', null=True, blank=True)
   date_create = models.DateTimeField(auto_now_add=True)
   date_update = models.DateTimeField(auto_now=True)
   sale_status = models.CharField(max_length=20, default='판매중')  # 판매여부(문자)
   display_order = models.IntegerField(default=0)  # 상위노출(숫자)
   
   def __str__(self):
       return f"{self.code}, {self.name}"
   
