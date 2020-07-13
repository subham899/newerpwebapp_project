from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'erpwebapp/index.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        messege=request.POST['message']
        send_mail(
            'NEW ERP WEBSITE',
            messege,
            settings.EMAIL_HOST_USER,
            ['subhambasu980@gmail.com'],

            fail_silently=False,
        )
        return render(request, 'erpwebapp/contact.html', {'name':name})
    else:
        return render(request, 'erpwebapp/contact.html')
