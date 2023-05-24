from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib import admin
from decimal import * 
from datetime import datetime

# Qr Code
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here. 

class Bulletin(models.Model):    
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.CharField(max_length=800, null=True, blank=True)
    bulletin_date = models.DateField('bulletin_date',null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    create_by = models.CharField(max_length=200, null=True, blank=True)

    # ...
    def __str__(self):
        return self.title

    @property
    def BulletinImgs(self):
        return (BulletinFile.objects.filter(bulletin_id= self.id).order_by('id'))

    @property
    def BulletinComnt(self):
        return (BulletinComment.objects.filter(bulletin_id= self.id).order_by('id'))

    @property
    def BulletinAknldg(self):
        return (Aknowledge.objects.filter(bulletin_id= self.id).order_by('id'))
    

class BulletinFile(models.Model):
    bulletin = models.ForeignKey(Bulletin, db_column="bulletin_id", related_name='bulletin_file', on_delete=models.CASCADE,null=True, blank=True)
    images = models.FileField(upload_to= "Bulletin/",null=True, blank=True)
    ext = models.CharField(max_length=200, null=True, blank=True)    
    upload_date = models.DateField('upload_date',null=True, blank=True)

class Aknowledge(models.Model):
    bulletin_title = models.CharField(max_length=200, null=True, blank=True)    
    bulletin = models.ForeignKey(Bulletin, db_column="bulletin_id", related_name='bulletin_viewed',null=True, on_delete=models.DO_NOTHING, blank=True)
    aknowledge_date = models.DateTimeField('upload_date',null=True, blank=True)
    status = models.CharField(max_length=100 ,null=True, blank=True)    
    create_by = models.CharField(max_length=200, null=True, blank=True)      
    create_by_id = models.IntegerField(null=True, blank=True)

class BulletinComment(models.Model):
    comment = models.CharField(max_length=200, null=True, blank=True)    
    bulletin = models.ForeignKey(Bulletin, db_column="bulletin_id", related_name='bulletin_comment',null=True, on_delete=models.CASCADE, blank=True)
    comment_date = models.DateTimeField('upload_date',null=True, blank=True)
    create_by = models.CharField(max_length=200, null=True, blank=True)

class AiportProject(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)     
    location = models.CharField(max_length=200, null=True, blank=True)     
    description = models.CharField(max_length=1000, null=True, blank=True)
    fund_particulars = models.CharField(max_length=1000, null=True, blank=True) 
    contract_desc = models.CharField(max_length=1000, null=True, blank=True) 
    profile = models.CharField(max_length=1000, null=True, blank=True) 
    status_desc = models.CharField(max_length=1000, null=True, blank=True) 
    slippage = models.CharField(max_length=200, null=True, blank=True) 
    amount = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal(0.00), blank=True)
    agency = models.CharField(max_length=200, null=True, blank=True) 
    status = models.CharField(max_length=1000, null=True, blank=True) 
    area = models.CharField(max_length=200, null=True, blank=True) 
    region = models.CharField(max_length=200, null=True, blank=True) 
    certificate = models.CharField(max_length=200, null=True, blank=True) 
    recouped_pay = models.CharField(max_length=200, null=True, blank=True)       
    progress = models.IntegerField(null=True, blank=True, default=0)
    edited_by = models.CharField(max_length=100, null=True, blank=True)
    date_edited = models.DateTimeField('editdate',null=True, blank=True)    
    date_created = models.DateTimeField('editdate',null=True, blank=True)

    # title = models.CharField(max_length=200, null=True, blank=True)     
    # location = models.CharField(max_length=200, null=True, blank=True)     
    # description = models.CharField(max_length=1000, null=True, blank=True)
    # fund_particulars = models.CharField(max_length=1000, null=True, blank=True) 
    # contract_desc = models.CharField(max_length=1000, null=True, blank=True) 
    # profile = models.CharField(max_length=1000, null=True, blank=True) 
    # status_desc = models.CharField(max_length=1000, null=True, blank=True) 
    # slippage = models.CharField(max_length=200, null=True, blank=True) 
    # amount = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal(0.00), blank=True)
    # agency = models.CharField(max_length=200, null=True, blank=True) 
    # status = models.CharField(max_length=1000, null=True, blank=True) 
    # area = models.CharField(max_length=200, null=True, blank=True) 
    # region = models.CharField(max_length=200, null=True, blank=True) 
    # certificate = models.CharField(max_length=200, null=True, blank=True) 
    # recouped_pay = models.CharField(max_length=200, null=True, blank=True)       
    # progress = models.IntegerField(null=True, blank=True)
    # edited_by = models.CharField(max_length=100, null=True, blank=True)
    # date_edited = models.DateTimeField('editdate',null=True, blank=True)    
    # date_created = models.DateTimeField('editdate',null=True, blank=True)

class AiportProfile(models.Model):
    airportuid = models.CharField(max_length=200, null=True, blank=True) 
    name = models.CharField(max_length=200, null=True, blank=True) 
    category = models.CharField(max_length=200, null=True, blank=True)
    crit_aircraft= models.CharField(max_length=200, null=True, blank=True) 
    icao_code= models.CharField(max_length=200, null=True, blank=True) 
    designation = models.CharField(max_length=200, null=True, blank=True) 
    nehca = models.CharField(max_length=200, null=True, blank=True) 
    runway_dimension = models.CharField(max_length=200, null=True, blank=True)
    runway_surface = models.CharField(max_length=200, null=True, blank=True) 
    runway_obstacles = models.CharField(max_length=200, null=True, blank=True) 
    runway_remarks = models.CharField(max_length=200, null=True, blank=True) 
    taxiway_dimension = models.CharField(max_length=200, null=True, blank=True) 
    taxiway_surface = models.CharField(max_length=200, null=True, blank=True) 
    taxiway_num = models.IntegerField(null=True, blank=True)
    taxiway_description = models.CharField(max_length=200, null=True, blank=True) 
    apron_dimension = models.CharField(max_length=200, null=True, blank=True) 
    apron_surface = models.CharField(max_length=200, null=True, blank=True)        
    apron_num = models.IntegerField(null=True, blank=True)
    ptb_dimension = models.CharField(max_length=200, null=True, blank=True) 
    ptb_aircon = models.CharField(max_length=200, null=True, blank=True) 
    ptb_toilet = models.CharField(max_length=200, null=True, blank=True) 
    tower = models.CharField(max_length=200, null=True, blank=True)  
    com_flight = models.CharField(max_length=200, null=True, blank=True)    
    note = models.CharField(max_length=200, null=True, blank=True)     
    profile_photo = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_photo.png", blank=True)
    profile_runway = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_runway.png", blank=True)
    profile_apron = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_apron.png", blank=True)
    profile_ptb = models.ImageField(upload_to= "airports_photo/", default="airports_photo/profile_ptb.png", blank=True)





    