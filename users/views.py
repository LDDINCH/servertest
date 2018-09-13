from django.shortcuts import render
from .models import UserMessage

def hello(request):
    return render(request, 'forms.html')

def handle(request):
    username = request.POST.get('username', '')
    mobile = request.POST.get('mobile')
    usermessage = UserMessage()
    usermessage.name = username
    usermessage.mobile = mobile
    usermessage.save()
    return render(request, 'hello.html')

# Create your views here.
