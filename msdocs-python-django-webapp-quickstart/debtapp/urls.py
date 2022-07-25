from django.urls import path
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('users/',users, name='users'),
    path("changecompany/<str:companyID>",changecompany, name='changecompany'),
    path("debtor-aging-detail/", agingdetail, name='debtoragingdetail'),
    path("ajaxreq/", ajaxreq, name='ajaxreq'),
    path('csv/',getfile, name='getfile'),  
    path('sm/',sm, name='sm')  
]