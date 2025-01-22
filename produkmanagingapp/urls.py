from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tambah_produk/', views.tambah_produk, name='tambah_produk'),
    path('ubah_produk/<int:pk>', views.ubah_produk, name='ubah_produk'),
    path('hapus_produk/<int:pk>', views.hapus_produk, name='hapus_produk'),
]
