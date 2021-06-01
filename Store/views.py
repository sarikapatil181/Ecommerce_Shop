from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def index(request):
    products=Product.get_all_products()
    categories=Category.get_all_categories()
    categoryID=request.GET.get('category')
    if categoryID:
        products=Product.get_products_categoryid(categoryID)
    else:
        products=Product.get_all_products()
    data={}
    data['products']=products
    data['categories']=categories
   # print(products)
    #return render(request,'orders/order.html')
    return render(request,'index.html',data)

def valiadteCustomer(customer):
        error_message=None
        if(not customer.first_name):
            error_message="First Name Required"
        elif len(customer.first_name)<4:
            error_message="frist Name must be 4 character long"
        elif(not customer.last_name):
            error_message="Last Name Required"
        elif len(customer.last_name)<4:
            error_message="Last Name must be 4 character long"
        elif(not customer.phone):
            error_message="Phone Number Required"
        elif len(customer.phone)<10:
            error_message="Phone Number Length should be 10 digit"
        elif(not customer.email):
            error_message="Email Required"
        elif customer.isExist():
            error_message="Email address already exist"
        elif (not customer.password):
            error_message="Password required"
        return error_message
def RegisterUser(request):
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        value={'first_name':first_name,'last_name':last_name,'phone':phone,'email':email}
        error_message=None
        customer=Customer(first_name=first_name,last_name=last_name,
            phone=phone,email=email,password=password)
        error_message=valiadteCustomer(customer)
                
        if not(error_message):
            
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request,"Signup.html",data)

def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
         return RegisterUser(request)
        
def login(request):
    if request.method=='GET':
        return render(request,'login.html')      
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_eamil(email)
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message="Email or password Invalid"
        else:
            error_message="Email or password Invalid"
        data={
                'error':error_message,
                
             }  
        return render(request,'login.html',data)
  
    