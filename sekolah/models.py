from django.db import models
from django.utils.translation import gettext_lazy as _

class jenissekolah(models.TextChoices):
    SMA = 'SMA', _('Sekolah Menengah Atas')
    SMK = 'SMK', _('Sekolah Menengah Kejuruan')
    UNIVERSITAS = 'UNIV', _('Perguruan Tinggi')

class sekolah(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True,null=True)
    web = models.CharField(max_length=100)
    hp = models.CharField(max_length=254, blank=True,null=True)
    alamat = models.TextField(default='Jawa Barat')
    jenis_sekolah = models.CharField(
        max_length=4,
        choices=jenissekolah.choices,
    )

    #default
    #create_by =
    create_at =models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
    