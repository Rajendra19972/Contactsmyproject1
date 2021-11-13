from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import details
# Create your views here.
def insert(request):
    id =request.POST['id']
    avatar = request.POST['link']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    phonenumber=request.POST['phonenumber']
    email = request.POST['email']
    company = request.POST['company']
    job_title = request.POST['job_title']

    k = details(id=id,avatar=avatar,last_name=last_name,phonenumber=phonenumber,email=email,company=company,job_title=job_title)
    k.save()
    return HttpResponseRedirect('/contacts')

def inputt(request):
    return render(request,'insert.html')

def contacts(request):
    data = details.objects.all()
    return render(request,'contacts.html',{'data':data})