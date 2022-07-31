from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is Homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About page")
    
def service(request, name):
    if name == amul :
        return render(request, 'about.html')
    # return HttpResponse("This is About page")

def amul(request):
    return render(request, 'amul.html')
    # return HttpResponse("This is Service page")

def thickshake(request):
    return render(request, 'thickshake.html')
    # return HttpResponse("This is Service page")
    
def maggi(request):
    return render(request, 'maggi.html')
    # return HttpResponse("This is Service page")
    
def chipotle(request):
    return render(request, 'chipotle.html')
    # return HttpResponse("This is Service page")
    
def ccd(request):
    return render(request, 'ccd.html')
    # return HttpResponse("This is Service page")
    
def wichplease(request):
    return render(request, 'wichplease.html')
    # return HttpResponse("This is Service page")
    
def yummpys(request):
    return render(request, 'yummpys.html')
    # return HttpResponse("This is Service page")
    
def nescafe(request):
    return render(request, 'nescafe.html')
    # return HttpResponse("This is Service page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact page")