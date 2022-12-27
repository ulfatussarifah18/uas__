from django.shortcuts import render
from .models import review

def rev(request):
    tah = review.objects.all()

    context = {
        'tah': tah,
    }

    return render(request,'review.html',context)
