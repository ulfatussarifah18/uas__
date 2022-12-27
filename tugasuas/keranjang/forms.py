from django.forms import ModelForm
from .models import keranjang

class form(ModelForm):
    class Meta:
        model = keranjang
        fields = '__all__'
