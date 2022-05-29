from django.shortcuts import render
from notification.models import Notification
from blood_type.models import BloodType
from request.models import Request
from student_register.models import StudentRegister
import  datetime
# Create your views here.
def notification(request,idd):
    mm=Request.objects.filter(req_id=idd)
    obj=BloodType.objects.all()
    context={
        'objval':obj,
        'req':mm
    }
    if request.method=="POST" and 'search' in request.POST:
        mp=request.POST.get('blood')
        print(mp)
        request.session['bid']=mp

        rr=request.POST.get('noti')
        request.session['nn']=rr

        bb=BloodType.objects.get(blood_id=mp)
        ob=StudentRegister.objects.filter(blood_type=bb.blood_type)
        con={
            'objj':ob,
        }
        return render(request,"notification/Notification.html",con)

    if request.method=="POST" and 'send' in request.POST:
        bbid=request.session['bid']
        print(bbid)
        mp=BloodType.objects.get(blood_id=bbid)
        obb = StudentRegister.objects.filter(blood_type=mp.blood_type).values_list('stud_id', flat=True)
        bd = BloodType.objects.get(blood_type=mp.blood_type)
        print(bd)
        for j in obb:
            od = Notification()
            od.notification = request.session['nn']
            od.blood_id = bd.blood_id
            od.stud_id = j
            od.date = datetime.date.today()
            od.time = datetime.datetime.now().strftime("%I:%M:%S")
            od.status='pending'
            od.save()
    return render(request,"notification/Notification.html",context)

def view_resp(request):
    obb=Notification.objects.all()
    context={
        'obj1':obb,
    }
    return render(request,"notification/view response.html",context)

def view_noti(request):
    obval=Notification.objects.all()
    context={
        'ob1':obval,
    }
    return render(request,"notification/view_notification.html",context)

def manage_noti(request):
    objj=Notification.objects.all()
    context={
        'obj1':objj,
    }
    return render(request,"notification/manage_notification.html",context)