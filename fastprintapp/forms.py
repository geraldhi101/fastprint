from django import forms
from .models import Produk, Kategori, Status

class ProdukForm(forms.ModelForm):
	nama_produk = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nama Produk", "class":"form-control"}), label="Nama Produk")
	harga = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Harga", "class":"form-control"}), label="Harga")

	class Meta:
		model = Produk
		fields = '__all__'
	
		class Meta:
			model = Kategori
			fields = '__all__'
			
		class Meta:
			model = Status
			fields = '__all__'