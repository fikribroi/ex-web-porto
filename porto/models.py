from django.db import models

# Create your models here.
    
class fitur(models.Model):
    fiturapp = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    about = models.TextField()
    bahasa = models.CharField(max_length=255)
    
class experience(models.Model):
    tahun = models.IntegerField()
    posisi = models.CharField(max_length=50)
    di = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    cerita = models.CharField(max_length=200)
    show = models.BooleanField(default=False)
    
class education(models.Model):
    tahun = models.IntegerField()
    universitas = models.CharField(max_length=50)
    cerita = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=50)
    lulusan = models.CharField(max_length=50)
    tempat = models.CharField(max_length=50)
    is_true = models.BooleanField()
    

class contact(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500)
    sendat = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.nama} - {self.email}'
  

class setting(models.Model):
    maintance = models.BooleanField(default=False)
      
    
class project(models.Model):
    nama = models.CharField(max_length=50)
    desk = models.CharField(max_length=50)
    models.ImageField(null=True, blank=True, upload_to="images/")    
