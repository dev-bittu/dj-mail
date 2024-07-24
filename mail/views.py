from django.shortcuts import redirect
from .models import *
from .mails import send_email
from django.http import JsonResponse

# Create your views here.
def send_mail(request, uid):
    if request.method == "POST":
        mail = Mail.objects.filter(uid=uid)
        if mail.exists():
            mail = mail[0]
            data = request.POST
            res = send_email(mail.email, data)
            
            return JsonResponse({
                "msg": "Done"
            })
    
    return redirect("https://bit.ly/cyberkernel")