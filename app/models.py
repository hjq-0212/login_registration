from django.db import models



class user_info(models.Model):

    user_id  = models.CharField(max_length=20),
    user_email = models.CharField(max_length=20)
    user_password =models.CharField(max_length=20),
    user_phone = models.IntegerField(),





