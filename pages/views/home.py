from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    error = False
    if request.user.is_active:
        return render_to_response('dashboard.html', {'username': request.user.username})
    elif 'username' and 'password' in request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return render_to_response('dashboard.html', {'username': request.user.username})
        else:
            error = True
    else:
        error = True
    return render_to_response('login.html', {'error': error})


@csrf_exempt
def login(request):
    return render_to_response('login.html')


@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect('/login')


@csrf_exempt
def error(request):
    return render_to_response('page_404.html')