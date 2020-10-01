from django.db import models

# Create your models here.
class Product(models.Model):
    ID = models.AutoField
    Name = models.CharField(max_length = 50)
    Price = models.CharField(max_length=20)
    desc = models.CharField(max_length=5000, default='')
    image = models.ImageField(upload_to='hackKovid/images')
    UploadToHINTLatestProductOrTOPSellingProducts = models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class Order(models.Model):
    country = models.CharField(max_length=50, default="")
    itemsJson = models.CharField(max_length=5000, default="")
    FirstName = models.CharField(max_length=30, default="")
    LastName = models.CharField(max_length=30, default="")
    address = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=20, default="")
    amount = models.CharField(max_length=20, default="")
    postNumber = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=20, default="")
    phone = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.FirstName