from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Fui(request):
    return render(request, 'Fui.html') 

def herb_page(request):
    return render(request, 'Herb.html') 

def fui_page(request):
    return render(request, 'Fui.html')