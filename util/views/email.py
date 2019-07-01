from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from env_page import models

# Create your views here.
@csrf_exempt
def SendMail(request):
    if not request.user.is_active:
        return redirect('/login')
    return render_to_response('util_email_sender.html', {'username': request.user.username,
                                                   })

@csrf_exempt
def EmailSubmit(request):
    if not request.user.is_active:
        return redirect('/login')
    receipts = request.POST.get('receipts')
    receipts = str(receipts)
    receiptList = receipts.split(";")

    return render_to_response('util_email_sent.html', {'username': request.user.username,
                                                   })