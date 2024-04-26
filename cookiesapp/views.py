from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,template_name='base.html')
def add(request):
    x = int(request.GET['t1'])
    y = int(request.GET['t2'])
    z = x+y
    resp = HttpResponse('value submited successfully')
    resp.set_cookie('z',z,max_age=100)
    return resp
def display(request):
    if 'z' in request.COOKIES:
        sum = request.COOKIES['z']
        return HttpResponse("admin of two no:"+sum)
    else:
        return HttpResponse("enter values")