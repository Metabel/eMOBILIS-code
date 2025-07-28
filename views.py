
# Create your views here.
from django.shortcuts import render
def index(request):
    skills=["html","cybersecurity","AI","python"]
    return render(request, "index.html",{'skills':skills})
    
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def example(request):
    student={
    "name":"Tracy",
    "age" :"19",
    "course":"MIT",
    "school":"eMobilis"
        
    }
    #passing a list
    
    return render(request,'demo.html')