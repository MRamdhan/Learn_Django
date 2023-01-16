from django.db import models
from django.utils.translation import gettext_lazy as _


class jeniskelamin(models.TextChoices):
    Laki_Laki = 'L', _('laki-laki')
    PEREMPUAN = 'P', _('perempuan')

# Create your models here.
class DataSiswa(models.Model):
    nisn =models.CharField(max_length=20)
    nama = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(
        max_length=1,
        choices=jeniskelamin.choices,
    )
    email = models.EmailField(max_length=254, blank=True,null=True)
    hp = models.CharField(max_length=254, blank=True,null=True)
    sekolah = models.OneToOneField("sekolah.sekolah",on_delete=models.CASCADE,blank=True,null=True)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    alamat = models.TextField(default='Jawa Barat')
    #sekolah

    #default
    #create_by =
    create_at =models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

