from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class statussekolah(models.TextChoices):
    SWASTA = 'Swasta', _('Swasta')
    NEGERI = 'Negeri', _('Negeri')

class sekolah(models.Model):
    npsn =models.CharField(max_length=50, default='')
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True,null=True)
    hp = models.CharField(max_length=254, blank=True,null=True)
    alamat = models.TextField(max_length=254, blank=True,null=True)
    provinsi = models.TextField(max_length=254, blank=True,null=True)
    kabupaten_kota= models.TextField(max_length=254, blank=True,null=True)
    status = models.CharField(
        max_length=10,
        choices=statussekolah.choices,
        null=False,
        default=''
    )

    #default
    create_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="sekolah_created_by")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        db_table = "sekolah"
        ordering = ["-id"]
        verbose_name_plural = "Sekolah"