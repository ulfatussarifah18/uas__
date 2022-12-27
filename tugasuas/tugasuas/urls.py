
from django.contrib import admin
from django.urls import path
from .import views
from home import views as homeviews
from keranjang import views as keranjangviews
from reviews import views as reviewsviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pembelian/',homeviews.pembeli),
    path('keranjang/',keranjangviews.keran),
     path('review/',reviewsviews.rev),
    path('',views.index),
]
