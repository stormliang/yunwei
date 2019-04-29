from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32)  # 书名
    price = models.CharField(max_length=32)  # 价格
    author = models.CharField(max_length=32)  # 作者
    publisher = models.CharField(max_length=32)  # 出版社
