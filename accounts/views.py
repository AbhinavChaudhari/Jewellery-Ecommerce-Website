from django.shortcuts import render
from .forms import CustomerRegistraitonForm,LoginForm
from django.views import View
from django.contrib import messages

# Create your views here.
# def login(request):
#     return render(request, 'Login.html')

# def register(request):
#     return render(request, 'register.html')

class CustomerRegistraitonView(View):
    def get(self,request):
        form = CustomerRegistraitonForm()
        return render(request, 'register/register.html',{'forms':form})

    def post(self,request):
        form = CustomerRegistraitonForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations... You succesufully registered ')
            form.save()
        return render(request, 'register/register.html',{'forms':form})


def changepass(request):
    return render(request, 'changepassword.html')
