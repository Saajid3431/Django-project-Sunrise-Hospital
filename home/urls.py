from django.urls import path, include
from . import views

urlpatterns =[
    path('',views.index, name='home'),
    # path('about/',views.about, name='about'),
    path('center/',views.center, name='centerofexcellence'),
    path('multispeciality/',views.multispeciality, name='multispeciality'),
    path('contact/',views.contact, name='contact'),
    path('doctors/',views.doctors, name='doctors'),
    path('booking/',views.booking, name='booking'),
    path('departments/',views.departments, name='departments'),
    path('markcloe/',views.markcloe, name='markcloe'),
    path('clara/',views.clara, name='clara'),
    path('afreen/',views.afreen, name='afreen'),
    path('simon/',views.simon, name='simon'),

    ]
