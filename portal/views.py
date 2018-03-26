from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'portal/index.html')

def product_lamp(request):
    return render(request,'portal/product_lamp.html')

def product_light(request):
    return render(request,'portal/product_light.html')

def product_municipal(request):
    return render(request,'portal/product_municipal.html')

def product_pip(request):
    return render(request,'portal/product_pip.html')

def contact_us(request):
    return render(request,'portal/contact_us.html')

def news_center(request):
    return render(request,'portal/news_center.html')

def company(request):
    return render(request,'portal/company.html')

def municipal(request):
    return render(request,'portal/municipal.html')

def news_list(request,news_date):
    return render(request,'portal/'+news_date+'.html')

