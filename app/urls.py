
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.HomepageView.as_view(),name="homepage"),
    path('productDetailView/<int:pk>',views.ProductDetailView.as_view(),name="productDetailView"),

    # ajax
    path('updateItem/',views.updateItem,name="updateItem"),
    path('getCategory/',views.getCategory,name="getCategory"),
    # path('getCart/',views.getCategory,name="getCart"),
    # ajax end

    path('aboutus/',views.aboutus,name="aboutus"),
    path('checkout/',views.checkout,name="checkout"),
    path('contact/',views.contact,name="contact"),
    
    path('newAddress/',views.newAddress,name="newAddress"),
   
    
    path('shop/<int:pk>',views.shop,name="shop"),
    path('wishlist',views.wishlist,name="wishlist"),
    path('cart/',views.cart,name="cart"),

 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)