from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class contect(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    number=models.IntegerField
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=2000)
    
    def __str__(self):
        return self.name
  
class app(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    number=models.IntegerField
    gender=models.CharField(max_length=100)
    adata=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name  
        
class sub(models.Model):
    email=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name        
        
    
class gallery(models.Model):
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to='pictures')
    des=models.TextField()
    date=models.DateField()
    class Meta:
        db_table="gallery"
        
class owner(models.Model):
    name=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    class meta:
        db_table='owner'
    def __str__(self):
        return self.name    
        
class worker(models.Model):
    name=models.CharField(max_length=40)
    salary=models.IntegerField()
    dept_id=models.ForeignKey(owner,on_delete=models.CASCADE)
    class meta:
        db_table='worker'
        
class dietplan(models.Model):
    title=models.CharField(max_length=5000)
    des=HTMLField()
    class Meta:
        db_table="dietplan"
        


