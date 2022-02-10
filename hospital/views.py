from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Doctor, Patient, Appointment

# Create your views here.



def Home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html',{
        "doctors": doctors
    }) 


def About(request):
    return render(request, 'about.html') 


def Contact(request):
    return render(request, 'contact.html') 

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d=0
    p=0
    a=0

    for i in doctor:
        d+=1

    for i in patient:
        p +=1
    
    for i in appointment:
        a +=1

    mycontext = {
        'doctor': d,
        'patient': p,
        'appointment': a,   
    }
    return render(request, 'index.html', mycontext)

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('admin_login')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)


def delete_doctor(request, did):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.get(id=did)
    doc.delete()
    return redirect('view_doctor')


def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        m = request.POST['mobile']
        s = request.POST['special']

        try:
            Doctor.objects.create(name=n, mobile=m, special=s)
            error = "no"
        
        except:
            error = "yes"
    d = {"error": error}
    return render(request, 'add_doctor.html', d)



def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.all()
    d = {'pat': patient}
    return render(request, 'view_patient.html', d)


def delete_patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.get(id=pid)
    pat.delete()
    return redirect('view_patient')


def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address = request.POST['address']

        try:
            Patient.objects.create(name=name, gender=gender, mobile=mobile, address=address)
            error = "no"
        
        except:
            error = "yes"
    d = {"error": error}
    return render(request, 'add_patient.html', d)


def view_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    a = {'app': appointment}
    return render(request, 'view_appointment.html', a)


def delete_Appointment(request, aid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=aid)
    appointment.delete()
    return redirect('view_appointment')

    

def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        p_name = request.POST['patient']
        d_name = request.POST['doctor']
        dat = request.POST['date']
        tim = request.POST['time']
        doc = Doctor.objects.filter(name=d_name).first()
        pat = Patient.objects.filter(name=p_name).first()
        try:
            Appointment.objects.create(doctor=doc, patient=pat, date=dat, time=tim)
            error = "no"
        except:
            error = "yes"
    d = {"doctor":doctor1, "patient":patient1, "error": error}
    return render(request, 'add_appointment.html', d)