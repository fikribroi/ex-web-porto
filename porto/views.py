from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import fitur, education, experience, contact, setting

# Create your views here.
def home(request):
    feature = fitur
    feature.nama = 'FikWeb'
    feature.about = 'Web dalam tahap pengembangan. Bertujuan untuk pembelajaran'
    return render(request, 'index.html', {'fitur': feature})



def kontak(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pesan = request.POST['pesan']

        if contact.objects.filter(email=email).exists():
            messages.info(request, 'anda sudah kontak sebelumnya')
            return redirect('kontak')
        else:

            contact.objects.create(
                nama=username,
                email=email,
                message=pesan,

            )
            messages.success(request, 'berhasil dikirim')
    return render(request, 'contact.html')

def masuk(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'account NOT FOUND')
            return redirect('login')

    return render(request, 'login.html')

'''
def resetpw(request):
    if request.method == 'POST':
        old_password = request.POST['correctpw']
        new_password = request.POST['newpw']

        if request.user.check_password(old_password):
            request.user.set_password(new_password)
            request.user.save()

            messages.success(request, "Password berhasil diubah.")
            return redirect('login')

        messages.error(request, "Password lama salah.")
        return redirect('resetpw')

    return render(request, 'resetpw.html')

'''

def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['user'].lower()
        email = request.POST['email']
        pw = request.POST['password']
        confirmpw =request.POST['repeatpw']
        if pw == confirmpw:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email sudah ada')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'User sudah ada')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=pw)
                user.is_staff = False
                user.is_superuser = False
                user.save()
                return redirect('login')
        else:
            messages.info('error')
            return redirect(request, 'register')

    return render(request, 'register.html')

def error404(request, exception):
    return render(request, "404.html", status=404)

def error500(request):
    return render(request, "500.html", status=500)

def out(request):
    logout(request)
    return redirect('/')

def resume(request):
    pendidikan = education.objects.all()
    experiencee = experience.objects.all()
    return render(request, 'resume.html',{'pendidikan': pendidikan,'pengalaman': experiencee})

def project(request):
    show = setting.objects.first()
    if show.maintance == True:
        return render(request, 'maintance.html' )
    else:
        return render(request, 'projects.html' )