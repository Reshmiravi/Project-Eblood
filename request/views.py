from django.shortcuts import render
from blood_type.models import BloodType
from hospital_bloodbank.models import HospitalBloodbank
from request.models import Request
import datetime

# Create your views here.
def request(request):
    objl=BloodType.objects.all()
    obj=HospitalBloodbank.objects.all()
    context={
        'obval':objl,
        'obb':obj,
    }
    if request.method=="POST":
        objj=Request()
        objj.blood_id=request.POST.get('blood')
        objj.date=datetime.date.today()
        objj.time=datetime.datetime.now()
        objj.hb_id=request.POST.get('ins')
        objj.type=request.POST.get('typ')
        objj.location=request.POST.get('loc')
        objj.save()
    return render(request,"request/Request.html",context)
    # return render(request,"request/Request.html")

def view_request(request):
    objj=Request.objects.all()
    context={
        'obv':objj,
    }
    return  render(request,"request/view_request.html",context)
def delete_request(request,idd):
    objj=Request.objects.get(req_id=idd)
    objj.delete()
    return view_request(request)

