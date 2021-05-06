from django.shortcuts import render

# Create your views here.
def order_med(request):
    return render(request,'order_med.html')