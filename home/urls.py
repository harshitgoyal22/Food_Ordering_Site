from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("amul", views.amul, name='amul'),
    path("maggi", views.maggi, name='maggi'),
    path("ccd", views.ccd, name='ccd'),
    path("wichplease", views.wichplease, name='wichplease'),
    path("chipotle", views.chipotle, name='chipotle'),
    path("yummpys", views.yummpys, name='yummpys'),
    path("thickshake", views.thickshake, name='thickshake'),
    path("nescafe", views.nescafe, name='nescafe'),
    path("contact", views.contact, name='contact'),
]
