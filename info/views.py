from django.shortcuts import render
from .models import Query_model
from .forms import Query_form , Contact_form
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return render (request,'index.html')

def about(request):
    return render (request,'about.html')

def blog(request):
    return render (request,'blog.html')

def contact(request):
    if request.method == "POST":
        fm = Contact_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Contact_form()
    else:
      fm = Contact_form()
    return render (request,'contact.html',{'form':fm})

def portfolio(request):
    return render (request,'portfolio.html')

def service(request):
    return render (request,'service.html')

def single(request):
    return render (request,'single.html')

def team(request):
    return render (request,'team.html')

def query(request):
    if request.method == "POST":
        fm = Query_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Query_form()
    else:
      fm = Query_form()
    return render (request,'query-page.html',{'form':fm})
