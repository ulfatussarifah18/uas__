from django.db import models

class keranjang(models.Model):
    Toko = models.CharField(max_length=50)
    Jumlah = models.CharField(max_length=10)
    Variasi = models.CharField(max_length=10)
    Pilihan = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.Pilihan)

