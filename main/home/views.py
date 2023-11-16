from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments, Doctors, Booking, Contact
from .forms import BookingForm, ContactForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirm.html')
    form = BookingForm()
    dict_forms = {
        'form': form
    }
    return render(request, 'booking.html', dict_forms)


def doctors(request):
    doc_data = {
        'doc': Doctors.objects.all()
    }
    return render(request, 'doctors.html', doc_data)


def contact(request):
   form=ContactForm()
   if request.method=='POST':
      form=ContactForm(request.POST)
      if form.is_valid():
         form.save()
         return render(request, 'confirm.html', {'delay_seconds': 5})
   form = ContactForm()
   c_forms={
      'form':form
   }
   
   return render(request, 'contact.html',c_forms)


def department(request):
    dep_data = {
        'dep': Departments.objects.all()
    }
    return render(request, 'department.html', dep_data)
