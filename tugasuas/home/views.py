from django.shortcuts import render
from .models import pembelian

def pembeli(request):
    blog = pembelian.objects.all()

    context = {
        'blog': blog,
    }
    return render(request,'pembelian.html',context)

