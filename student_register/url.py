from django.conf.urls import url
from student_register import views
urlpatterns=[
    url('manage profile/',views.manage_profile),
    url('manage_student/',views.manage_stud),
    url('stud_register/',views.register),
    url('view_student/',views.view_student),
    url('reject/(?P<idd>\w+)',views.reject_students,name='reject')

]