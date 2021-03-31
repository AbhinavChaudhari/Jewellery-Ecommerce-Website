from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Addresses(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    houseNo = models.CharField(max_length=200,null=True,blank=True)
    area = models.CharField(max_length=200,null=True,blank=True)
    landmark = models.CharField(max_length=200,null=True,blank=True)
    mobileNo = models.CharField(max_length=120,null=True,blank=True)
   
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    date = models.DateField(auto_created=True)





class Category(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="catergory",null=True,blank=True)
    date = models.DateField(auto_created=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="SubCategory" ,null =True ,blank=True)
    show = models.BooleanField(default=False)
    date  = models.DateField(auto_created=True)
    def __str__(self):
        return str(self.category.name) +"  "+ str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=100)
    dsp= models.TextField(max_length=2000)
    price = models.IntegerField()
    D_price = models.IntegerField()
    sale = models.BooleanField(default=False)
    subCategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE ,null=True,blank=True)
    image_1 = models.ImageField(upload_to='product') 
    image_2 = models.ImageField(upload_to='product', blank=True, null = True) 
    image_3 = models.ImageField(upload_to='product', blank=True, null = True) 
    image_4 = models.ImageField(upload_to='product', blank=True, null = True) 
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    
    

STATUS_CHOICES=(
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey(Addresses,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE ,null=True,blank=True)
    subtotal = models.IntegerField(null=True,blank=True )
    qty = models.IntegerField(null=True,blank=True )
    shipping = models.IntegerField(null=True,blank=True)
    Total = models.IntegerField(null=True,blank=True)
    orderDate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100 ,choices=STATUS_CHOICES,default='Pending')
  
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    dsp = models.TextField(max_length=2000)
    photo = models.ImageField(upload_to='Testimonial')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class MainCaraousalAd(models.Model):
    FirstLine = models.CharField(max_length=1000,null=True,blank=True)
    SecondLine = models.CharField(max_length=1000,null=True,blank=True)
    ThirdLine = models.CharField(max_length=1000,null=True,blank=True)
    pic = models.ImageField(upload_to='mainAdvertise')
    visible = models.BooleanField(default=False )
    date = models.DateField(auto_now_add=True)

    
class RevieOfProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    

    

    

    
    

