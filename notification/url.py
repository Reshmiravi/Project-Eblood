from django.conf.urls import url
from notification import views
urlpatterns=[
    url('add_notification/(?P<idd>\w+)',views.notification,name='add_notify'),
    url('view_response/',views.view_resp),
    url('view_notification/',views.view_noti),
    url('manage_notification/',views.manage_noti),
]