from django.db import models
from django.contrib.auth.models import User

class SozlukContent(models.Model):

    orn = models.CharField(max_length=9999,verbose_name="orn")
    ekleyen = models.CharField(max_length=255,verbose_name="ekleyen")
    artikel = models.CharField(max_length=3,verbose_name="artikel")
    kategori = models.CharField(max_length=50,verbose_name="kategori")
    plural_wort_status = models.CharField(max_length=50,verbose_name="plural_wort_status")
    asw_de = models.CharField(max_length=9999,verbose_name="asw_de")
    asw_tr = models.CharField(max_length=9999,verbose_name="asw_tr")
    tr = models.CharField(max_length=255,verbose_name="tr")
    en = models.CharField(max_length=255,verbose_name="en")
    de = models.CharField(max_length=255,verbose_name="de")
    referans_video = models.CharField(max_length=500,verbose_name="referans_video")
    tr_def = models.CharField(max_length=500,verbose_name="tr_def")
    de_def = models.CharField(max_length=500,verbose_name="de_def")
    active = models.IntegerField(verbose_name="active")
    ekleyenId = models.OneToOneField(User,on_delete=models.CASCADE)
    abz_de = models.CharField(max_length=500,verbose_name="abz_de")
    abz_tr = models.CharField(max_length=500,verbose_name="abz_tr")
    synm_de = models.CharField(max_length=500,verbose_name="synm_de")
    synm_tr = models.CharField(max_length=500,verbose_name="synm_tr")
    anmerkungen_de = models.CharField(max_length=500,verbose_name="anmerkungen_de")
    anmerkungen_tr = models.CharField(max_length=500,verbose_name="anmerkungen_tr")
    kontext_de = models.CharField(max_length=500,verbose_name="kontext_de")
    kontext_tr = models.CharField(max_length=500,verbose_name="kontext_tr")

    def __str__(self):
        return self.de
