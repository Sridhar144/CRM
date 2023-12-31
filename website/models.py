from django.db import models

# Create your models here.
class Record(models.Model):
    sno=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=10)
    def __str__(self):
            return(f"{self.first_name} {self.last_name}")