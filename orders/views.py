from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models.orders import Order
from .models.prescriptions import Prescription
from accounts.models.customers import Customer
import json
from PayTm import Checksum
from .forms import PrescriptionForm
from django.views.decorators.csrf import csrf_exempt
MERCHANT_KEY='xmttI_EUX&#uMIul'
# order=None

# Create your views here.
def checkout(request):
    if request.method=="POST":
        if request.session.get('email')!=None:
            items_json= request.POST.get('itemsJson', '')
            name=request.POST.get('name', '')
            email=request.POST.get('email', '')
            address=request.POST.get('address', '') + " " + request.POST.get('address2', '')
            city=request.POST.get('city', '')
            state=request.POST.get('state', '')
            pin_code=request.POST.get('pin', '')
            phone=request.POST.get('phone', '')
            total_amount=request.POST.get('amount', '')
            total_amount=total_amount.strip()
            # print(total_amount)
            # print(type(total_amount))
            customer_id = request.session.get('customer_id','')
            customer=Customer.objects.get(id=customer_id)

            # myDate = datetime.now()
            # formatedDate = myDate.strftime("%d-%B-%Y  %H:%M:%S")
            # global order
            order = Order(customer_id=customer,
                          name=name,
                          items= items_json,
                          email=email,
                          address= address,
                          city=city,
                          state=state,
                          pin_code=pin_code,
                          phone=phone,
                          update_desc="Your order has been placed",
                          total_amount=total_amount)
            order.save()
            # thank=True
            # id=order.order_id
            # print(order.order_id)
            # return render(request, 'checkout.html', {'thank':thank, 'id':id})
            # Request paytm to transfer the amount to your account after payment by user
            param_dict = {

                'MID': 'sInAQD47479049988843',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(total_amount),
                'CUST_ID': 'email',
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/orders/handlerequest/',

            }
            param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)

            return render(request, 'paytm.html', {'param_dict': param_dict})
            # return render(request, 'checkout.html')
        else:
            return render(request,'login.html')
    else:
        return render(request, 'checkout.html')

def tracker(request):
        customer_id=request.session.get('customer_id')
        updates = []
        try:
            order=Order.objects.filter(customer_id=customer_id)
            for item in order:
                updates.append(([item,json.loads(item.items)]))
            return render(request, 'track_order.html',{'updates':updates})
        except Exception as e:
            return render(request, 'track_order.html', {'updates':updates})

@csrf_exempt
def handlerequest(request):
    '''paytm will send you post request here.'''
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            # global order
            # order.save()
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})

def uploadPrescription(request):
    if request.method=='POST':
        if request.session.get('email') != None:
            prescription=request.FILES['myfile']

            customer_id = request.session.get('customer_id', '')
            customer = Customer.objects.get(id=customer_id)

            medOrder = Prescription.objects.create(customer_id=customer,
                             prescription=prescription)

            medOrder.save()
            thank = True
            return render(request, 'order_med.html', {'thank': thank})

            # form=PrescriptionForm(request.POST,request.FILES)
            # if form.is_valid():
            #     form.save()
            #     thank=True
            #     return render(request,'order_med.html',{'thank':thank})
        else:
            return render(request, 'login.html')
    else:
        thank=False
        return render(request, 'order_med.html', {'thank': thank})