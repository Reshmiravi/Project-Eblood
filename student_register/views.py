from django.shortcuts import render
from student_register.models import StudentRegister
from blood_type.models import BloodType

# Create your views here.
def manage_profile(request):
    obj=StudentRegister.objects.all()
    context={
        'obval':obj
    }
    return render(request,"register/manage_profile.html",context)

def manage_stud(request):
    obj=StudentRegister.objects.all()
    context={
        'objj':obj
    }
    return render(request,"register/manage_student.html",context)

def register(request):
    if request.method == "POST":
        obj = StudentRegister()
        obj.username = request.POST.get('user')
        obj.password = request.POST.get('pass')
        obj.full_name = request.POST.get('name')
        obj.email_id = request.POST.get('mail')
        obj.phone_no = request.POST.get('num')
        obj.whatsapp_no = request.POST.get('watsp')
        obj.course_name = request.POST.get('course')
        obj.gender = request.POST.get('gender')
        obj.address = request.POST.get('address')
        obj.age = request.POST.get('age')
        obj.blood_type = request.POST.get('blood')
        obj.weight = request.POST.get('weight')
        obj.disease = request.POST.get('diag')
        obj.last_date = request.POST.get('dona')
        obj.save()
        ob=BloodType()
        ob.blood_type= request.POST.get('blood')
        ob.stud_id=obj.stud_id
        ob.save()
    return render(request,"register/Register.html")


def view_student(request):
    obj = BloodType.objects.all()
    context = {
        'objval': obj,
    }
    if request.method=="POST":
        v=request.POST.get('blood')
        ob=StudentRegister.objects.filter(blood_type=v)
        bgrp={
            'val':ob,
        }
        return render(request, "register/view_student.html", bgrp)

    return render(request, "register/view_student.html", context)
def reject_students(request,idd):
    obb=StudentRegister.objects.get(stud_id=idd)
    obb.delete()
    return view_student(request)

