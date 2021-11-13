from django.db import models

# Create your models here.
class details(models.Model):
    id = models.IntegerField(primary_key=True)
    avatar = models.TextField(default="No Description")
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phonenumber=models.IntegerField()
    email = models.EmailField(max_length=50)
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)