from django.shortcuts import render
from app123.models import pysp

# Create your views here.
def storedata(request):
    if request.method == 'POST':
        a = request.POST['sid']
        b =request.POST['name']
        c = request.POST['mobile']
        d = request.POST['email']
        e = request.POST['password']
        pysp.objects.create(sid = a, name = b, mobile = c, email = d, password = e)
        return render(request,'html1.html')
    return render(request,'index.html')