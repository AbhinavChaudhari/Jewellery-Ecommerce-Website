from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import random
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def Editadr(request,id):
    if request.method == "POST":
        ad = Addresses.objects.get(id=id)
        ad.first_name = request.POST["first_name"]
        ad.last_name = request.POST["last_name"]
        ad.mobileNo = request.POST["mobileNo"]
        ad.houseNo = request.POST["house"]
        ad.area = request.POST["area"]
        ad.landmark = request.POST["landmark"]
        ad.city = request.POST["city"]
        ad.state = request.POST["state"]
        ad.pin = request.POST["pincode"]
        ad.date = datetime.datetime.today()
        ad.save()
        return redirect('address')

    else:
        adr = Addresses.objects.get(id=id)
        return render(request, 'Address/adr_edit.html',{'adr':adr})

@login_required
def address(request):
    user = request.user
    adr = Addresses.objects.filter(user=user)
    return render(request, 'Address/address.html',{'adr':adr})

@login_required
def newAddress(request):
    if request.method =="POST": 
        add = Addresses()
        user = request.user
        add.user = user
        add.first_name = request.POST["first_name"]
        add.last_name = request.POST["last_name"]
        add.houseNo = request.POST["house"]
        add.area = request.POST["area"]
        add.landmark = request.POST["landmark"]
        add.mobileNo = request.POST["mobileNo"]       
        add.state = request.POST["state"]
        add.city = request.POST["city"]
        add.pin = request.POST["pincode"]
        add.date = datetime.datetime.today()
        add.save()
        return redirect('address')
    else:
        return render(request,"Address/newAddress.html")

def getCartQty(request):
    user = request.user
    if user.is_authenticated:
        
        cart = Cart.objects.filter(user=user).values()
    else:
        cart = {}
    return JsonResponse({'cart':list(cart)},safe=False)
        


def getCategory(request):
    data = SubCategory.objects.all().values()
    cat = Category.objects.all().values()
    user = request.user
    if user.is_authenticated:
        cart = Cart.objects.filter(user=user).values()
    else:
        cart = {}
    return JsonResponse({'data':list(data),'cart':list(cart),'cat':list(cat)},safe=False)

@login_required
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


@login_required()
def order(request):
    user = request.user
    order = Order.objects.filter(user=user)
    return render(request,'order/order.html',{'order':order})

@login_required
def checkout(request):
    total = 0
    shipping =70
    user = request.user
    cart = Cart.objects.filter(user =user)
        
    for i in cart:
        if i.qty <= 1:
            total = total + i.product.D_price
    
        else:
            total = total + (i.product.D_price * i.qty)
    if request.method =="POST":
        odr= Order()
        
        ids=request.POST['adr']
        adrs = Addresses.objects.get(user=user,id=ids)
        
        cart = Cart.objects.filter(user=user)
        
        for c in cart:
            Order(user=user, product=c.product,qty=c.qty ,address=adrs,Total=total+shipping,shipping=shipping,subtotal=total,status="Pending").save()
            c.delete()
        return redirect("homepage")

    else:
        # to show  details of in checkout page 
        
        adr = Addresses.objects.filter(user=user)
        
        return render(request,"checkout.html",{'adr':adr,'cart':cart,"subtotal":total})




def contact(request):
    return render(request,'contact-us.html')

def blogdetail(request):
    return render(request,'blog-details.html')

def login(request):
    return render(request,'login-register.html')







def wishlist(request):
    return render(request,'wishlist.html')

def cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    total = 0
    for i in cart:
        if i.qty <= 1:
            total = total + i.product.D_price
 
        else:
            total = total + (i.product.D_price * i.qty)
  
    return render(request,"cart.html",{'carts':cart,'total':total})



@csrf_exempt
def get_qty_update(request):
    if request.is_ajax():
        data =  request.POST.get('data')
        jd = json.loads(data)
        if jd['action'] =="add":
            prid = int(jd['productId'])
            cart = Cart.objects.get(id=prid,user=request.user)
            cart.qty = int(cart.qty) +int(1)
            cart.save()
            return JsonResponse({'data':"qty increament"})
        
        elif jd['action'] =="dec":
            prid = int(jd['productId'])
            cart = Cart.objects.get(id=prid,user=request.user)
        
            if cart.qty == '1':
                return JsonResponse({'data':"We cannot reduce value"})
            cart.qty = int(cart.qty) - int(1)
            cart.save()
            return JsonResponse({'data':"qty decrement"})
