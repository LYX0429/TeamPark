from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from pages import models
from django.utils import timezone
from pages import form

# Create your views here.
@csrf_exempt
def form(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "appointment":
        objs = models.Appointment.objects.all
        return render_to_response('table_appointment.html', {'username': request.user.username,
                                                   'objs': objs,})
    return render_to_response('page_404.html')


@csrf_exempt
def edit(request, object_type, object_id):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "appointment":
        object_id = int(object_id)
        try:
            target = models.Appointment.objects.get(id=object_id)
        except:
            return render_to_response('page_404.html')
        dockers = models.Doctor.objects.all
        return render_to_response('edit_appointment.html', {'username': request.user.username,
                                                       'target': target,
                                                       'dockers': dockers,})
    return render_to_response('page_404.html')

@csrf_exempt
def new_edit(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    elif object_type == "appointment":
        dockers = models.Doctor.objects.all
        return render_to_response('edit_appointment.html', {'username': request.user.username,
                                                       'dockers': dockers,})
    return render_to_response('page_404.html')

@csrf_exempt
def new_edit2(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    elif object_type == "appointment":
        dockers = models.Doctor.objects.all
        return render_to_response('edit2_appointment.html', {'username': request.user.username,
                                                       'dockers': dockers,})
    return render_to_response('page_404.html')

@csrf_exempt
def submit(request, object_type, object_id):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "appointment":
        object_id = int(object_id)
        new_obj = models.Appointment(
            id=object_id,
            name=request.POST.get('name'),
            birthday=request.POST.get('birthday'),
            injury=request.POST.get('injury'),
            comment=request.POST.get('comment'),
            date=timezone.now()
        )
        new_obj.doctor = models.Doctor.objects.get(id=request.POST.get('doctor'))
        new_obj.save()
        return redirect('../../')
    return render_to_response('page_404.html')


@csrf_exempt
def new_submit(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "appointment":
        return redirect('../../new2/')
    return render_to_response('page_404.html')

@csrf_exempt
def new_submit2(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "appointment":
        new_obj = models.Appointment(
            date=request.POST.get('date')
        )
        new_obj.doctor = models.Doctor.objects.get(id=request.POST.get('doctor'))
        new_obj.save()
        return redirect('../../')
    return render_to_response('page_404.html')

@csrf_exempt
def delete(request, object_type, object_id):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "appointment":
        object_id = int(object_id)
        models.Appointment.objects.get(id=object_id).delete()
        return redirect('../../')
    return render_to_response('page_404.html')


@csrf_exempt
def new_delete(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    return redirect('../../')