from django.test import TestCase
from .models import sekolah

class sekolahTestCase(TestCase):
    def setUp(self):
        sekolah.objects.create(npsn="2026822X", nama="SMKN 2 ", status="Negeri")
    
    def test_sekolah_cek_nama(self):
        """ Cek nama sekolah """
        smkn2 = sekolah.objects.get(nama="SMKN 2 ")
        self.assertEqual(smkn2.nama, "SMKN 2 ")