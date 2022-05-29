from django.conf.urls import url
from request import views
urlpatterns=[
    url('add_request/',views.request),
    url('view_request/',views.view_request),
    url('delete/(?P<idd>\w+)', views.delete_request, name='delete'),

]