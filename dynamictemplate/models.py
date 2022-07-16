from django.db import models
from dynamictemplate.filefield import ContentRestrictionFileField
from django.core.validators import MaxValueValidator,MinValueValidator


"""
Note : When you use ContentRestrictionFileField height and width are optional field to be added .
if you don't specify them then thei value is by default treated as 0 and there will be no check in dimensions of the image File

"""
# Create your models here.
class Logo(models.Model):
    logo_name = models.CharField(max_length=10)
    # 88 X 23 
    logo_image = ContentRestrictionFileField(
        upload_to="logo/",
        max_upload_size =1000000,
        content_types=["image/jpeg", "image/png", "image/JPG", "image/jpg"],
        null=True,
        blank=True,
        default=None,
        )
    active_status = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)

    def __str__(self):
        return self.logo_name
    

class ContactAddress(models.Model):
    company_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255,null=True,blank=True,default=None)
    contact_1 = models.CharField(max_length=14)
    contact_2 = models.CharField(max_length=14,null=True,blank=True,default=None)
    email_1 = models.EmailField(max_length=50)
    email_2 = models.EmailField(max_length=50,null=True,blank=True,default=None)
    google_embedding_link = models.URLField(max_length=500)
    active_status = models.BooleanField()
    date_added = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.company_name


class CarosulData(models.Model):
    headline = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    
    # 1920 X 720
    headline_image = ContentRestrictionFileField(
    upload_to="carosul/",
    max_upload_size =1000000,
    content_types=["image/jpeg", "image/png", "image/JPG", "image/jpg"],
    width=1920,
    height = 720,
    null=True,
    blank=True,
    default=None,
    max_length=500,
    )
    special_offer = models.CharField(max_length=255)
    active_status = models.BooleanField()
    offer_discount = models.IntegerField(null=True,blank=True,validators=[MaxValueValidator(100),MinValueValidator(0)])
    