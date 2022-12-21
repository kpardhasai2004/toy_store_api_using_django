from django.shortcuts import render,redirect
from .models import items
# Create your views here.
from django.http import HttpResponse

def home(request):
	return render(request,'home.html')

def upload(request):
    if request.method == 'POST':
        idno = request.POST['idno']
        name = request.POST['name']
        company = request.POST['company']
        price = request.POST['price']
        quantity = request.POST['quantity']
        i= items(idno=idno,name=name,company=company,price=price,quantity=quantity)
        i.save()
        return redirect('dashboard')
    return render(request,'upload.html')

def dashboard(request):
        item = items.objects.all()
        return render(request,'dashboard.html',{'item':item})

def delete(request, id):
    if request.method == 'POST':
        items.objects.get(id=id).delete()
    return redirect('dashboard')

def update(request, id):
    if request.method == 'POST':
        idno = request.POST.get('idno',False)
        name = request.POST.get('name',False)
        company = request.POST.get('company',False)
        price = request.POST.get('price',False)
        quantity = request.POST.get('quantity',False)
        items.objects.filter(id=id).update(idno=idno,name=name,company=company,price=price,quantity=quantity)
        return render(request,'update.html')
    return redirect('dashboard')