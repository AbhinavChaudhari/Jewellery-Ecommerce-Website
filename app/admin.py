from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display =['id','houseNo','area','landmark','city','state','pin','date']

@admin.register(Category)
class CatergoryAdmin(admin.ModelAdmin):
    list_display=['id','name','date']

@admin.register(SubCategory)
class SubCatergoryAdmin(admin.ModelAdmin):
    list_display=['id','name','date','category']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','D_price','sale','subCategory','image_1']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display =['id','qty','user','product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id','subtotal','shipping','Total','status']

@admin.register(MainCaraousalAd)
class MainCaraousalAdAdmin(admin.ModelAdmin):
    list_display=['id','FirstLine','date','visible']
