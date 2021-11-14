from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import details
from myapp1 import forms
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

    k = details(id=id,avatar=avatar,first_name=first_name,last_name=last_name,phonenumber=phonenumber,email=email,company=company,job_title=job_title)
    k.save()
    return HttpResponseRedirect('/contacts')

def inputt(request):
    return render(request,'insert.html')

def contacts(request):
    data = details.objects.all()
    return render(request,'contacts.html',{'data':data})
def update(request,id):
    id1 = details.objects.get(id=id)
    form1 = forms.detaisform(request.POST or None, instance=id1)
    if form1.is_valid():
        form1.save()
        return redirect('/contacts')
    return render(request, 'update.html', context={'form1': form1})
def delete(request,id):
    id2 = details.objects.get(id=id)
    id2.delete()
    return redirect('/contacts')