from datetime import datetime
from django.shortcuts import render, HttpResponse
from myApp.models import Contact
from django.contrib import messages
# import datetime

# Create your views here.


def base(request):
    # return HttpResponse('HEllO Home')
    # content={
    #    'name':'ANIRBAN MISHRA',
    #    'age':'20',
    #    'course':'DJANGO'
    # }
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    # return HttpResponse('About')
    return render(request, 'about.html')


def contact(request):
    # return HttpResponse('Contact')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('ph')
        desc = request.POST.get('desc')
        print(name, email)
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        # contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Message sent successfully !')

    return render(request, 'contact.html')
