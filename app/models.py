from django.db import models



class user_info(models.Model):

    account  = models.CharField(max_length=20)   #账号
    email = models.EmailField()                  #邮箱
    password =models.CharField(max_length=20)    #密码






