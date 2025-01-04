from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from DentalApp.models import Doctor
# from app_admin.models import Doctor
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def doctor(request):
    doctors = Doctor.objects.all()
    template = loader.get_template('home/doctor.html')
    context = {
        'doctors': doctors,
    }
    return HttpResponse(template.render(context, request))