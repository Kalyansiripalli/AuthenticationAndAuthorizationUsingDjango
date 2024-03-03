from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data=[
        {
            'name':'kalyan',
            'age':23,
        },
        {
            'name':'kumar',
            'age':33,
        },
        {
            'name':'ramanna',
            'age':2,
        },
        {
            'name':'jyosthna',
            'age':3,
        },
    ]
    return render(request, "home/index.html", context={"data":data,"pagename":"homepage"})

def about(request):
    return render(request,"home/about.html", context={"pagename":"aboutpage"})
def contactUs(request):
    return render(request,"home/contactUs.html",context={"pagename":"contactpage"})

