from django.shortcuts import render
from.forms import form

def keran(request):
    cor = form()
    context = {
        'cor': cor,
    }
    return render(request,'keranjang.html',context)
