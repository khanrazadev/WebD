from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"raza/index.html")




def wvideos(request):
    return render(request,"raza/wvideos.html")
def channels(request):
    return render(request,"raza/channels.html")
def category(request):
    return render(request, "raza/category.html")
def stars(request):
    return render(request, "raza/stars.html")