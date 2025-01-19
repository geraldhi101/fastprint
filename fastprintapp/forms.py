from django import forms
from .models import Produk, Kategori, Status

PILIHAN_STATUS = {
	"b" : "Bisa dijual",
	"t" : "Tidak bisa dijual"
}

class TambahProduk(forms.ModelForm):
	nama_produk = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nama Produk", "class":"form-control"}), label="Nama Produk")
	harga = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Harga", "class":"form-control"}), label="Harga")

	class Meta:
		model = Produk
		fields = '__all__'
	
	class KategoriForm(forms.ModelForm):
		kategori = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Kategori", "class":"form-control"}), label="Kategori")

		class Meta:
			model = Kategori
			fields = '__all__'
			
	class StatusForm(forms.ModelForm):
		status = forms.ChoiceField(required=True, widget=forms.widgets.RadioSelect(), label="Status", choices=PILIHAN_STATUS)

		class Meta:
			model = Status
			fields = '__all__'