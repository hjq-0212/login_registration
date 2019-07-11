from django.db import models



class user_info(models.Model):

    account  = models.CharField(max_length=20)
    email = models.EmailField()
    password =models.CharField(max_length=20)






