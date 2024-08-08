#added
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,related_name='patient')
    p_Firstname=models.CharField(max_length=50)
    p_Lastname=models.CharField(max_length=50)
    p_Picture=models.ImageField(upload_to='images/')
    p_Username=models.CharField(max_length=20)
    p_EmailId=models.CharField(max_length=50)
    p_Password=models.CharField(max_length=20)
    p_AddressLi=models.TextField()
    p_City=models.CharField(max_length=25)
    p_State=models.CharField(max_length=25)
    p_Pincode=models.CharField(max_length=14)

class doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,related_name='doctor')
    d_Username=models.CharField(max_length=20)
    d_Firstname=models.CharField(max_length=50)
    d_Lastname=models.CharField(max_length=50)
    d_Picture=models.FileField(upload_to='images/')
    d_Password=models.CharField(max_length=20)
    d_EmailId=models.CharField(max_length=50)
    d_AddressLi=models.TextField()
    d_City=models.CharField(max_length=25)
    d_State=models.CharField(max_length=25)
    d_Pincode=models.CharField(max_length=14)
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)

class imagePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    iTitle = models.CharField(max_length=255)
    iImage = models.ImageField(upload_to='images/')
    iCategory = models.CharField(max_length=50)  # Keep as CharField
    iSummary = models.TextField()
    iContent = models.TextField()
    is_draft = models.BooleanField(default=False)  # Indicates if the post is a draft

    def __str__(self):
        return self.iTitle

class appointmentData(models.Model):
    ap_username=models.CharField(max_length=20)
    ap_specilist=models.CharField(max_length=30)
    ap_date=models.DateField()
    ap_startTime=models.TimeField()
    ap_endTime=models.DateTimeField()
