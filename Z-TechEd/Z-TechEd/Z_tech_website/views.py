from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Z_tech_website/index.html')
def about(request):
    return render(request,'Z_tech_website/about.html')