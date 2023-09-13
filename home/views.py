from django.shortcuts import render
from django.http import HttpResponse
# from.models import About
from.models import Doctors, Departments
from.forms import Bookingform





# Create your views here.
def index(request):
    dict_doc ={
        'doctors': Doctors.objects.all()
    }
    return render(request,"index.html",dict_doc)

# def about(request):
#     dict_about={
#         'about': About.objects.all()
#     }
#     return render(request,"about.html",dict_about)

def departments(request):
    dict_dept={
        'departments': Departments.objects.all()
    }
    return render(request,"departments.html",dict_dept)



def multispeciality (request):
    return render(request,"multispeciality.html")

def center(request):
    return render( request,"center.html")

def contact(request):
    return render(request,"contact.html")

def doctors(request):
    dict_doc ={
        'doctors': Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_doc)

def booking(request):
    if request.method =="POST":
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
    form = Bookingform()
    dict_form={
        'form' : form
    }
    return render(request,"booking.html",dict_form)

def markcloe(request):
    return render(request,"markcloe.html")

def clara(request):
    return render(request,"clara.html")


def afreen(request):
    return render(request,"afreen.html")

def simon(request):
    return render(request,"simon.html")


