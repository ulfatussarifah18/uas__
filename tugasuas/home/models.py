from django.db import models

class pembelian(models.Model):
    Nama = models.CharField(max_length=50)
    Size = models.CharField(max_length=5)
    Harga = models.CharField(max_length=30)
    Ongkir = models.CharField(max_length=30)
    M_pembayaran = models.CharField(max_length=50)

    def __str__(self):
        return"{}. {}".format(self.Nama,self.Size)

