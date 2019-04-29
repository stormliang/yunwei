from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='书名')  # 书名
    price = models.CharField(max_length=32, verbose_name='价格')  # 价格
    author = models.CharField(max_length=32, verbose_name='作者')  # 作者
    publisher = models.CharField(max_length=32, verbose_name='出版社')  # 出版社


class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
