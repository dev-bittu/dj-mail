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
            res = send_email(mail.email, mail.subject, data)
            
            return JsonResponse({
                "msg": "done" if res == 1 else "failed"
            })
    
    return redirect("https://bit.ly/cyberkernel")