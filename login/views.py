from django.shortcuts import render
# Create your views here.
from login.models import Login
def login(request):
    # if request.method == "POST":
    #     uname = request.POST.get("user")
    #     passw = request.POST.get("pass")
    #     obj = Login.objects.filter(username=uname, password=passw)
    #     tp = ""
    #     for ob in obj:
    #         tp = ob.type
    #         uid = ob.stud_id
    #         if tp == "admin":
    #             request.session["u_id"] = uid
    #             return render(request, 'temp/index.html')
    #         elif tp == "registered_user":
    #             request.session["u_id"] = uid
    #             return render(request, 'temp/registered user.html')
    #         # elif tp == "user":
    #         #     request.session["u_id"] = uid
    #         #     return render(request, 'temp/user.html')
    #         # elif tp == "assistant":
    #         #     request.session["u_id"] = uid
    #         #     return render(request, 'temp/assistant.html')
    #         # else:
    #     objlist = "Username or Password incorrect... Please try again...!"
    #     context = {
    #         'msg': objlist,
    #     }
    #     return render(request, 'login/login.html', context)
    return render(request,"login/login.html")