from django.contrib import admin
from django.contrib import admin
from .models import DataSiswa
# Register your models here.
class siswa(admin.ModelAdmin):
    list_display = ['nama', 'email', 'hp', 'alamat', 'jenis_kelamin', 'sekolah','tempat_lahir','tanggal_lahir','nisn','create_at','update_at']
admin.site.register(DataSiswa,siswa)

