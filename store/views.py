from django.shortcuts import render
from .models.supplements import Supplement
from math import ceil


# Create your views here.
def index(request):
    return render(request,'index.html')

def searchMatch(query,item):
    query=query.lower()
    '''return true only if query matches the item'''
    if query in item.description.lower() or query in item.name.lower():
        return True
    else:
        return False


def search(request):
    query=request.GET.get('search')
    print(len(query))
    allSup = []
    catsup = Supplement.objects.values('category', 'id')
    cats = {item['category'] for item in catsup}
    for cat in cats:
        suptemp = Supplement.objects.filter(category=cat)
        sup=[item for item in suptemp if searchMatch(query,item)]
        n = len(sup)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(sup)!=0:
            allSup.append(([sup, range(1, nSlides), nSlides]))
            params = {'allSup': allSup,"msg":""}
    if len(allSup)==0 or len(query)<2:
        params={'msg':"Please make sure to enter relavant search query."}
    return render(request, 'search.html', params)

def healthcare_products(request):
    # supplements = Supplement.objects.all()
    # print(supplements)
    # n=len(supplements)
    # nSlides=n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides,'range':range(1,nSlides),'supplement':supplements}
    # allSup = [[supplements,range(1,nSlides),nSlides],
    #           [supplements,range(1,nSlides),nSlides]]
    allSup = []
    catsup=Supplement.objects.values('category','id')
    cats={item['category'] for item in catsup}
    for cat in cats:
        sup=Supplement.objects.filter(category=cat)
        n=len(sup)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allSup.append(([sup,range(1,nSlides),nSlides]))
    params={'allSup':allSup}
    return render(request,'healthcare_products.html',params)

def spview(request,spid):
    #fetching the product using the id
    supplement = Supplement.objects.filter(id=spid)
    return render(request,'healthcare_Prod_View.html',{'supplement':supplement[0]})

def aboutUs(request):
    return render(request,"about_us.html")