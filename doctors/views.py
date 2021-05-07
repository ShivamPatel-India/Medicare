from django.shortcuts import render
from .models.doctors import Doctor
from .models.conditions import Condition
from .models.procedures import Procedure

# Create your views here.
def findDr(request):
    allDoc = []
    Doc = Doctor.objects.all()
    for item in Doc:
        allDoc.append((item))
    params = {'allDoc': allDoc}
    print(allDoc)
    return render(request, 'find_dr.html', params)
    # return render(request,'find_dr.html')

def emergency(request):
    return render(request,'emerg.html')

def drview(request,drid):
    doctor = Doctor.objects.filter(id=drid)
    return render(request, 'dr_profile.html', {'doctor': doctor[0]})

def cnview(request,cnid):
    condition = Condition.objects.filter(id=cnid)
    return render(request, 'codition_view.html', {'condition': condition[0]})

def prview(request,prid):
    procedure = Procedure.objects.filter(id=prid)
    return render(request, 'procedure_view.html', {'procedure': procedure[0]})

def searchMatch(query,item):
    query=query.lower()
    '''return true only if query matches the item'''
    # dept=[i for i in item.department.all()]
    # print(dept)
    if query in item.last_name.lower() or query in item.area_of_focus.lower() or query in str(item.city).lower():
        return True
    else:
        return False


def DrSearch(request):
    query=request.GET.get('search')
    allDr = []
    deptDr = Doctor.objects.values('city', 'id')
    depts = {item['city'] for item in deptDr}
    for dept in depts:
        drTemp = Doctor.objects.filter(city=dept)
        doctors=[item for item in drTemp if searchMatch(query,item)]
        if len(doctors)!=0:
            allDr.append(doctors)
            params = {'allDr': allDr,"msg":""}
    if len(allDr)==0 or len(query)<2:
        params={'msg':"No result found! Please make sure to enter relavant search query."}
    return render(request, 'dr_search.html', params)
