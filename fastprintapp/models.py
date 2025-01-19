from django.db import models

# Create your models here.
class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(unique=True)
    harga = models.DecimalField(decimal_places=0, max_digits=5)
    kategori = models.ForeignKey('Kategori', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField()

    def __str__(self):
        return(f"{self.nama_kategori}")

class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField()

    def __str__(self):
        return(f"{self.nama_status}")