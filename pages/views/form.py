from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from pages import models

# Create your views here.
@csrf_exempt
def upload(request):
    if not request.user.is_active:
        return redirect('/login')
    return render_to_response('env_form_upload.html', {'username': request.user.username,
                                                   })