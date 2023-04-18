from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm
from .models import Detail_user, User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

def detail(request):
    if request.method == 'POST':
        if request.POST.get('Firstname') and request.POST.get('Lastname') and request.POST.get('Lastname'):
            user = request.user
            detail_user = Detail_user(user=request.user)
            detail_user.Firstname = request.POST.get('Firstname')
            detail_user.Lastname = request.POST.get('Lastname')
            detail_user.coursename = request.POST.get('coursename')

            detail_user.save()

    return render(request, 'users/detail.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        mobile_number=request.POST['mobile_number']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username exist')
            elif User.objects.filter(email=email).exists():
                print('username taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name,mobile_number=mobile_number)
                user.save()
                print('user created')
        else:
            print('password not matching')
        return redirect('/')
    else:
        return render(request, 'users/register.html')


def verification(request):
    certificate_objects = Detail_user.objects.all()

    certificateid = request.GET.get('certificate_id')
    if certificateid != '' and certificateid is not None:
        certificate = certificate_objects.filter(certificate_id=certificateid).values_list('certificate_id',
                                                                                           flat=True).first()
        if certificateid == certificate:
            validation = Detail_user.objects.filter(certificate_id=certificateid)
            print(validation)
            return render(request, 'users/valid2.html', {'validation': validation})

    return render(request, 'users/valid.html', )


@login_required(login_url='/')
def Getcertificate(request):
    course_objects = Detail_user.objects.all()
    Coursename = request.GET.get('coursename')
    if Coursename != '' and Coursename is not None:
        course = course_objects.filter(coursename=Coursename).values_list('coursename', flat=True).first()
        if Coursename == course:
            certificate_detail = Detail_user.objects.filter(Q(user=request.user) & Q(coursename=Coursename))
            print(certificate_detail)
            return render(request, 'users/certificate2.html', {'certificate_detail': certificate_detail})
        else:
            return HttpResponse('not working')

    return render(request, 'users/certificate.html', )
