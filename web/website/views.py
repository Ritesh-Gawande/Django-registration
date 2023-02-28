from django.shortcuts import render
from django.http import HttpResponse 
from .models import PostModelss
from django.shortcuts import redirect
# from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['mobile']
        city = request.POST['city']
        state = request.POST['state']
        new = PostModelss.objects.create(f_name=firstname,l_name=lastname,mail=email,mobile=phone,city=city,state=state)
        new.save
        return redirect('/')
    else :
        return render(request,'register.html')

