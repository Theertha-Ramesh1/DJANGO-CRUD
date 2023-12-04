from django.db import models

# Create your models here.
class Login(models.Model):
    F_Name = models.CharField(max_length=200)
    L_Name = models.CharField(max_length=200)
    Email =models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)

    class Meta:
        db_table = "Login"
