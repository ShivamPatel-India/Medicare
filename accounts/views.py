from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models.customers import Customer
from .models.contactUs import Contact_u
from django.views import View
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def postRequest(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    contact_no = request.POST['contact_no']
    email = request.POST['your_email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    value = {
        'first_name': first_name,
        'last_name': last_name,
        'contact_no': contact_no,
        'email': email
    }
    err_msg = None
    if password == confirm_password:
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            contact_no=contact_no,
                            email=email,
                            password=password)
        # validation
        err_msg = customer.validateCustomer()
    else:
        err_msg = "passwords did not match!"

    if not err_msg:
        customer.password = make_password(customer.password)
        customer.rgstr()
        return render(request,'login.html')
    else:
        data = {
            'err': err_msg,
            'values': value
        }
        return render(request, 'register.html', data)


def register(request):
    if request.method == 'POST':
        return postRequest(request)
    else:
        return render(request, 'register.html')


class Login(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.verify_customer(email)
        err_msg = None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_fname']=customer.first_name
                request.session['email'] = customer.email
                return redirect('/')
            else:
                err_msg = "Incorrect email or password!"
                return render(request, 'login.html', {'err': err_msg})
        else:
            err_msg = "Incorrect email or password!"
            return  render(request,'login.html',{'err':err_msg})

def logout(request):
    request.session.clear()
    return redirect('/')

def profile(request):
    customer_id=request.session.get('customer_id')
    customer_profile=Customer.objects.filter(id=customer_id)
    # print(customer_profile[0])
    return render(request,"your_profile.html",{'user': customer_profile[0]})

def edit_profile(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_no = request.POST['contact_no']
        email = request.POST['your_email']
        customer_id = request.session.get('customer_id')
        customer = Customer.objects.get(id=customer_id)
        customer.first_name=first_name
        customer.last_name=last_name
        customer.contact_no=contact_no
        customer.email=email
        customer.save()
        return render(request,'index.html',{'save':True})
    else:
        customer_id=request.session.get('customer_id')
        customer=Customer.objects.filter(id=customer_id)
        return render(request,"edit_profile.html",{'user': customer[0]})

def contact_us(request):
    if request.session.get('customer_id') != None:
        if request.method=='POST':
            email=request.POST.get('your_email')
            message=request.POST.get('message')
            print(email)
            customer_id = request.session.get('customer_id')
            customer = Customer.objects.get(id=customer_id)
            contact=Contact_u.objects.create(name=customer,email=email,message=message)
            contact.save()
            return render(request,"index.html",{'thank':True})
        else:
            return render(request, 'contact_us.html')
    else:
        return render(request,'login.html')