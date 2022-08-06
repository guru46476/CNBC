from django.contrib import messages
from sre_constants import CATEGORY
from django.shortcuts import render
import requests
from django.conf import settings
from django.core.mail import send_mail
from .models import *

API_KEY = 'a8299d0861964d7598f7ef860ff73c6b'


def categoryPage(request,name):
    response = requests.get(f'https://newsapi.org/v2/everything?q={name}&language=hi&apiKey=a8299d0861964d7598f7ef860ff73c6b').json()
    a = response['articles']
    return render(request, "index.html", {"Data":a,'category':name})

def categoryPageEng(request,name):
    url = f'https://newsapi.org/v2/everything?q={name}&language=en&apiKey=a8299d0861964d7598f7ef860ff73c6b'
    data = requests.get(url)
    response = data.json()
    a = response['articles']
    return render(request, "english.html", {"EngData":a,'category':name})    


def hindiPage(request):
    search = request.GET.get('search')
    if search:
        data = requests.get(
            f'https://newsapi.org/v2/everything?q={search}&language=hi&apiKey=a8299d0861964d7598f7ef860ff73c6b').json()
        a = data['articles']
    else:
        data = requests.get(
            f'https://newsapi.org/v2/everything?q=All&language=hi&apiKey=a8299d0861964d7598f7ef860ff73c6b').json()
        a = data['articles']

    return render(request, "index.html", {"Data": a})


def englishPage(request):
    search = request.GET.get('search')
    if search:
        data = requests.get(
            f'https://newsapi.org/v2/everything?q={search}&language=en&apiKey=a8299d0861964d7598f7ef860ff73c6b').json()
        a = data['articles']
    else:
        data = requests.get(
            f'https://newsapi.org/v2/everything?q=All&language=en&apiKey=a8299d0861964d7598f7ef860ff73c6b').json()
        a = data['articles']
    return render(request, "english.html", {"EngData": a})


def aboutPage(request):
    return render(request,"about.html")    

def contectPage(request):
    if(request.method=='POST'):
        c = Contect()
        c.name = request.POST.get('name')
        c.email = request.POST.get('email')
        c.subject = request.POST.get('subject')
        c.message = request.POST.get('message')
        c.save()
        subject = "Your Quary Has Been Submitted : Team CNBC_News"
        message = """
                    Thanks to Share Your Quary With Us
                    Our Team Will Contect You Soon
                    Team : CNBC_News
                    Keep Updated With Us
                    http://localhost:8000
                """
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [c.email,]
        send_mail(subject, message, email_from, recipient_list )

        messages.success(request,"Your Quary Has Been Submitted!!! Our Team Will Contect You Soon.")
    return render(request,"contect.html")  

def cnbcPage(request):
    # resourse = requests.get(f"http://api.mediastack.com/v1/news?access_key=3c372b03e3194cfb7ca7744d93ed5283&categories=sports,-business,-health,-science").json() 
    # news = resourse['data']  
    search = request.GET.get('search')
    if search:
        data = requests.get(
            f'https://newsapi.org/v2/everything?q={search}&language=en&apiKey=a8299d0861964d7598f7ef860ff73c6b').json()
        a = data['articles']
    else:
        data = requests.get(
            f'https://newsapi.org/v2/everything?q=bbc&language=en&apiKey=a8299d0861964d7598f7ef860ff73c6b').json()
        a = data['articles']
    return render(request, "cnbc.html",{"Data":a}) 
    

    