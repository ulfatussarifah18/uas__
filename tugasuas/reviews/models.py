from django.db import models

class review(models.Model):
    Ulasan = models.TextField( blank=True)
    Tampilan = models.CharField(max_length=50)
    Warna = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.Ulasan)
