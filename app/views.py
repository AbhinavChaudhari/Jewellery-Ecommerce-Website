from django.shortcuts import render
from django.views import View
from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import random



def getCategory(request):
    data = SubCategory.objects.all().values()
    cat = Category.objects.all().values()
    cart = Cart.objects.all().values()
    return JsonResponse({'data':list(data),'cart':list(cart),'cat':list(cat)},safe=False)


def updateItem(request):
    data =  request.POST.get('data')
    jd = json.loads(data)
    
    if jd['action'] =='add':
        if Cart.objects.filter(product__id = jd['productId']).exists(): #update cart with same product add
            product = Product.objects.get(id = jd['productId'])
            cart=(Cart.objects.get(product=product))
            print(cart.qty)
            cart.qty = int(cart.qty) +int(1)
            cart.save()
            return JsonResponse({"msg":f'Your is update qty'},safe=False)
        else:
            product = Product.objects.get(id=jd['productId']) #new product add to cart
            user = request.user
            cart = Cart()
            cart.product = product
            cart.user = user 
            cart.save()
            return JsonResponse({"msg":f'Your {product.name} is added to Cart'},safe=False)
    elif jd["action"]=='remove':        # Remove product from Cart
        product = Product.objects.get(id=jd['productId'])
        cart = Cart.objects.filter(product = product)
        cart.delete()
        return JsonResponse({"msg":f'Your {product.name} is Removed'},safe=False)

def shop(request,pk):
    if request.method =="GET":
        subcategory = SubCategory.objects.get(id = pk)
        product = Product.objects.filter(subCategory=subcategory)
    return render(request,"shop.html",{'product':product,"cat":subcategory})

class ProductDetailView(View):
    def get(self,request,pk):
        product= Product.objects.get(pk = pk)
        rlt = Product.objects.filter(subCategory=product.subCategory)
        
        return render(request,"product-details.html",{"product":product,'rlt':rlt})

class HomepageView(View):
    def get(self,request):
        items = list(Product.objects.all())
        product = random.sample(items, len(items))
        subcat = SubCategory.objects.all()
        adds = MainCaraousalAd.objects.all()
        return render(request,"index.html",{'product':product,'subcat':subcat,'adds':adds})




def aboutus(request):
    return render(request,"about-us.html")

def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,'contact-us.html')

def blogdetail(request):
    return render(request,'blog-details.html')

def login(request):
    return render(request,'login-register.html')

def newAddress(request):
   
    if request.method =="POST":
        if "saveAddress" in request.POST:
            add = Addresses()
            add.user = request.user
            add.first_name = request.POST["first_name"]
            add.last_name = request.POST["last_name"]
            add.address = request.POST["addr"]
            add.mobileNo = request.POST["mobileNo"]
            add.state = request.POST["state"]
            add.city = request.POST["city"]
            add.pin = request.POST["pincode"]

            add.save()
            return redirect('homepage')
    else:
        return render(request,"Address/newAddress.html")






def wishlist(request):
    return render(request,'wishlist.html')

def cart(request):
    cart = Cart.objects.all()
    return render(request,"cart.html",{'carts':cart})