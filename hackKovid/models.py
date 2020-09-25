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