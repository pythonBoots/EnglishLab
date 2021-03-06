from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    now = datetime.now()

    return render(
        request,
        "test_pass/index.html",
        {
            'title': "Hello Django!",
            'message': "Hello Django!", 
            'content': " on "  + now.strftime("%A,%d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "test_pass/about.html",
        {
            'title': "About test-pass",
            'content': "Example app page for Django"
            }
        )
