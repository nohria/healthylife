from django.shortcuts import render,redirect
from lifestyle.models import *
from lifestyle.forms import *
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
    return render(request,"intex.html")
    
def app(request):
    return render(request,"app.html")    

def about(request):
    return render(request,"about.html")
    
def services(request):   
    return render(request,"services.html")
    
def diet(request): 
    dt=dietplan.objects.all()
    context={'dt':dt}
    return render(request,"diet.html",context)   
    
def contectpage(request):
   
    return render(request,"contect.html")
    
 
def recipes(request):   
    return render(request,"recipes.html")

def breakfast(request):   
    return render(request,"breakfast.html")

def lunch(request):   
    return render(request,"lunch.html")

def dinner(request):   
    return render(request,"dinner.html")    
    
def snacks(request):   
    return render(request,"snacks.html")    
    
def apply(request):
    if request.method == "POST":
        if request.POST.get('message'):
            c = contect()
            c.name = request.POST.get('name')
            c.email = request.POST.get('email')
            c.number = request.POST.get('number')
            c.subject = request.POST.get('subject')
            c.message = request.POST.get('message')
            c.save()
    return render(request, 'contect.html') 


def suba(request):
    if request.method == "POST":
        if request.POST.get('email'):
            s.email = request.POST.get('email')
            s.save()
    return render(request, 'home.html') 



def blog(request):
    gly=gallery.objects.all()
    context={'gly':gly}
    return render(request,'blog.html',context)
    
def home(request):
    gly=gallery.objects.all()[0:4]
    context={'gly':gly}
    return render(request,'intex.html',context)
    
def blogdetals(request,id):
    gly=gallery.objects.get(id=id)
    context={'gly':gly}
    return render(request,'blogs.html',context)    
    
def sign(request):
    if request.method=='POST':
        form=signForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/app/')
    else:
        form=signForm()
    return render(request,'registration/sign.html',{'form':form})