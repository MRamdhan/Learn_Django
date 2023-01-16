from django.db import models
from django.utils.translation import gettext_lazy as _

class jenisperusahaan(models.TextChoices):
    Perseorangan ='Per', _('Perseorangan')
    CV ='CV', _('CV')
    PT ='PT', _('PT')
    Koperasi = 'Kop', _('Koperasi')
    Firma = 'FMA', _('Firma')
    Persero = 'Peo', _('Persero')

# Create your models here.
class perusahaan(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True,null=True)
    web = models.CharField(max_length=100)
    hp = models.CharField(max_length=254, blank=True,null=True)
    alamat = models.TextField(default='Jawa Barat')
    jenis_perusahaan = models.CharField(
        max_length=3,
        choices=jenisperusahaan.choices,
    )
    #default
    #create_by =
    create_at =models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
    
