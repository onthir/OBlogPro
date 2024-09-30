from django.db import models

# Create your models here.

class Type(models.Model):
    type_c = models.CharField(max_length=100)

    def __str__(self):
        return self.type_c

class Download(models.Model):
    category = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=150)
    date = models.DateField()
    description = models.TextField(max_length=1000)
    version = models.FloatField(null=True, blank=True)
    main_image = models.URLField(max_length=1000)
    image1 = models.URLField(max_length=1000, null=True, blank=True)
    image2= models.URLField(max_length=1000, null=True, blank=True)
    image3 = models.URLField(max_length=1000, null=True, blank=True)
    download_link = models.URLField(max_length=1000)
    downloads = models.IntegerField()

    def __str__(self):
        return self.name

