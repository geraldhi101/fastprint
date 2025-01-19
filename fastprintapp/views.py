from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ProdukForm
from .models import Produk, Status

# Create your views here.
def index(request):
    status = Status.objects.all()
    if request.GET.get('filter'):
        produk_filter = request.GET.get('filter')
        produk = Produk.objects.filter(status=produk_filter).order_by('id_produk')
        return render(request, 'index.html', {'produk':produk, 'status':status})
    else:
        produk = Produk.objects.all().order_by('id_produk')
        return render(request, 'index.html', {'produk':produk, 'status':status})
        

def tambah_produk(request):
    form = ProdukForm(request.POST or None)
    request.method = "POST"
    if form.is_valid():
        tambah_produk = form.save()
        messages.success(request, "Produk Berhasil Ditambah...")
        return redirect('index')
    return render(request, 'produk-tambah.html', {'form':form})
	
def ubah_produk(request, pk):
    produk_saat = Produk.objects.get(id_produk=pk)
    form = ProdukForm(request.POST or None, instance=produk_saat)
    if form.is_valid():
        form.save()
        messages.success(request, "Produk Berhasil Diubah...")
        return redirect('index')
    return render(request, 'produk-ubah.html', {'form':form})

def hapus_produk(request, pk):
    hapus = Produk.objects.get(id_produk=pk)
    hapus.delete()
    messages.success(request, "Produk berhasil Dihapus...")
    return redirect('index')
