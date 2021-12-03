from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from pages import models
from django.utils import timezone
from pages import form

# Create your views here.
@csrf_exempt
def env(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "project":
        projects = models.Project.objects.all
        return render_to_response('env_table_project.html', {'username': request.user.username,
                                                   'projects': projects,})
    elif object_type == "network":
        networks = models.Network.objects.all
        return render_to_response('env_table_network.html', {'username': request.user.username,
                                                   'networks': networks,})
    elif object_type == "product":
        products = models.Product.objects.all
        return render_to_response('env_table_product.html', {'username': request.user.username,
                                                   'products': products,})
    elif object_type == "server":
        servers = models.Server.objects.all
        return render_to_response('env_table_server.html', {'username': request.user.username,
                                                   'servers': servers,})
    elif object_type == "userinfo":
        userinfos = models.UserInfo.objects.all
        return render_to_response('env_table_userinfo.html', {'username': request.user.username,
                                                   'userinfos': userinfos,})
    return render_to_response('page_404.html')


@csrf_exempt
def edit(request, object_type, object_id):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "project":
        object_id = int(object_id)
        try:
            target = models.Project.objects.get(id=object_id)
        except:
            return render_to_response('page_404.html')
        return render_to_response('env_edit_project.html', {'username': request.user.username,
                                                       'target': target, })
    elif object_type == "product":
        object_id = int(object_id)
        try:
            target = models.Product.objects.get(id=object_id)
        except:
            return render_to_response('page_404.html')
        return render_to_response('env_edit_product.html', {'username': request.user.username,
                                                       'target': target, })
    elif object_type == "server":
        object_id = int(object_id)
        try:
            target = models.Server.objects.get(id=object_id)
        except:
            return render_to_response('page_404.html')
        projects = models.Project.objects.all
        products = models.Product.objects.all
        return render_to_response('env_edit_server.html', {'username': request.user.username,
                                                       'target': target,
                                                       'projects': projects,
                                                       'products': products,})
    elif object_type == "userinfo":
        object_id = int(object_id)
        try:
            target = models.UserInfo.objects.get(id=object_id)
        except:
            return render_to_response('page_404.html')
        servers = models.Server.objects.all
        return render_to_response('env_edit_userinfo.html', {'username': request.user.username,
                                                       'target': target,
                                                       'servers': servers,})
    elif object_type == "network":
        object_id = int(object_id)
        try:
            target = models.Network.objects.get(id=object_id)
        except:
            return render_to_response('page_404.html')
        servers = models.Server.objects.all
        return render_to_response('env_edit_network.html', {'username': request.user.username,
                                                       'target': target,
                                                       'servers': servers,})
    return render_to_response('page_404.html')


@csrf_exempt
def new_edit(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "project":
        return render_to_response('env_edit_project.html', {'username': request.user.username})
    elif object_type == "product":
        return render_to_response('env_edit_product.html', {'username': request.user.username})
    elif object_type == "server":
        projects = models.Project.objects.all
        products = models.Product.objects.all
        return render_to_response('env_edit_server.html', {'username': request.user.username,
                                                           'projects': projects,
                                                           'products': products,})
    elif object_type == "userinfo":
        servers = models.Server.objects.all
        return render_to_response('env_edit_userinfo.html', {'username': request.user.username,
                                                           'servers': servers,})
    elif object_type == "network":
        servers = models.Server.objects.all
        return render_to_response('env_edit_network.html', {'username': request.user.username,
                                                           'servers': servers,})
    return render_to_response('page_404.html')


@csrf_exempt
def submit(request, object_type, object_id):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "project":
        object_id = int(object_id)
        new_project = models.Project(
            id=object_id,
            project_name=request.POST.get('project_name'),
            project_desc=request.POST.get('project_desc'),
            update_date=timezone.now()
        )
        try:
            new_project.create_date = models.Project.objects.get(id=object_id).create_date
        except:
            new_project.create_date = timezone.now()
        new_project.save()
        return redirect('../../')
    elif object_type == "product":
        object_id = int(object_id)
        new_product = models.Product(
            id=object_id,
            product_name=request.POST.get('product_name'),
            product_desc=request.POST.get('product_desc'),
            update_date=timezone.now()
        )
        try:
            new_product.create_date = models.Product.objects.get(id=object_id).create_date
        except:
            new_product.create_date = timezone.now()
        new_product.save()
        return redirect('../../')
    elif object_type == "server":
        object_id = int(object_id)
        new_server = models.Server(
            id=object_id,
            server_name=request.POST.get('server_name'),
            ilo_ip=request.POST.get('ilo_ip'),
            server_desc=request.POST.get('server_desc'),
            server_type=request.POST.get('server_type'),
            server_vendor=request.POST.get('server_vendor'),
            update_date=timezone.now()
        )
        new_server.project.set(request.POST.getlist('project'))
        new_server.product.set(request.POST.getlist('product'))
        try:
            new_server.create_date = models.Server.objects.get(id=object_id).create_date
        except:
            new_server.create_date = timezone.now()
        new_server.save()
        return redirect('../../')
    elif object_type == "userinfo":
        object_id = int(object_id)
        new_network = models.UserInfo(
            id=object_id,
            user_name=request.POST.get('user_name'),
            user_desc=request.POST.get('user_desc'),
            password=request.POST.get('password'),
            update_date=timezone.now(),
        )
        try:
            new_network.create_date = models.Server.objects.get(id=object_id).create_date
        except:
            new_network.create_date = timezone.now()
        new_network.server = models.Server.objects.get(id=request.POST.get('server'))
        new_network.save()
        return redirect('../../')
    elif object_type == "network":
        object_id = int(object_id)
        new_network = models.Network(
            id=object_id,
            network_name=request.POST.get('network_name'),
            network_desc=request.POST.get('network_desc'),
            vlan=request.POST.get('vlan'),
            bond=request.POST.get('bond'),
            ethnet=request.POST.get('ethnet'),
            bridge_name=request.POST.get('bridge_name'),
            ipv4=request.POST.get('ipv4'),
            ipv4_prefix=request.POST.get('ipv4_prefix'),
            ipv4_gw=request.POST.get('ipv4_gw'),
            ipv6=request.POST.get('ipv6'),
            ipv6_prefix=request.POST.get('ipv6_prefix'),
            ipv6_gw=request.POST.get('ipv6_gw'),
            update_date=timezone.now(),
        )
        try:
            new_network.create_date = models.Server.objects.get(id=object_id).create_date
        except:
            new_network.create_date = timezone.now()
        new_network.server = models.Server.objects.get(id=request.POST.get('server'))
        new_network.save()
        return redirect('../../')
    return render_to_response('page_404.html')


@csrf_exempt
def new_submit(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "project":
        new_project = models.Project(
            project_name=request.POST.get('project_name'),
            project_desc=request.POST.get('project_desc'),
            update_date=timezone.now(),
            create_date=timezone.now(),
        )
        new_project.save()
        return redirect('../../')
    elif object_type == "product":
        new_product = models.Product(
            product_name=request.POST.get('product_name'),
            product_desc=request.POST.get('product_desc'),
            update_date=timezone.now(),
            create_date=timezone.now(),
        )
        new_product.save()
        return redirect('../../')
    elif object_type == "server":
        new_server = models.Server(
            server_name=request.POST.get('server_name'),
            ilo_ip=request.POST.get('ilo_ip'),
            server_desc=request.POST.get('server_desc'),
            server_type=request.POST.get('server_type'),
            server_vendor=request.POST.get('server_vendor'),
            update_date=timezone.now(),
            create_date=timezone.now(),
        )
        new_server.save()
        new_server.project.set(request.POST.getlist('project'))
        new_server.product.set(request.POST.getlist('product'))
        new_server.save()
        return redirect('../../')
    elif object_type == "userinfo":
        new_network = models.UserInfo(
            user_name=request.POST.get('user_name'),
            user_desc=request.POST.get('user_desc'),
            password=request.POST.get('password'),
            update_date=timezone.now(),
            create_date=timezone.now(),
        )
        new_network.server = models.Server.objects.get(id=request.POST.get('server'))
        new_network.save()
        return redirect('../../')
    elif object_type == "network":
        new_network = models.Network(
            network_name=request.POST.get('network_name'),
            network_desc=request.POST.get('network_desc'),
            vlan=request.POST.get('vlan'),
            bond=request.POST.get('bond'),
            ethnet=request.POST.get('ethnet'),
            bridge_name=request.POST.get('bridge_name'),
            ipv4=request.POST.get('ipv4'),
            ipv4_prefix=request.POST.get('ipv4_prefix'),
            ipv4_gw=request.POST.get('ipv4_gw'),
            ipv6=request.POST.get('ipv6'),
            ipv6_prefix=request.POST.get('ipv6_prefix'),
            ipv6_gw=request.POST.get('ipv6_gw'),
            update_date=timezone.now(),
            create_date=timezone.now(),
        )
        new_network.server = models.Server.objects.get(id=request.POST.get('server'))
        new_network.save()
        return redirect('../../')
    return render_to_response('page_404.html')


@csrf_exempt
def delete(request, object_type, object_id):
    if not request.user.is_active:
        return redirect('/login')
    if object_type == "project":
        object_id = int(object_id)
        models.Project.objects.get(id=object_id).delete()
        return redirect('../../')
    elif object_type == "product":
        object_id = int(object_id)
        models.Product.objects.get(id=object_id).delete()
        return redirect('../../')
    elif object_type == "server":
        object_id = int(object_id)
        models.Server.objects.get(id=object_id).delete()
        return redirect('../../')
    elif object_type == "userinfo":
        object_id = int(object_id)
        models.UserInfo.objects.get(id=object_id).delete()
        return redirect('../../')
    elif object_type == "network":
        object_id = int(object_id)
        models.Network.objects.get(id=object_id).delete()
        return redirect('../../')
    return render_to_response('page_404.html')


@csrf_exempt
def new_delete(request, object_type):
    if not request.user.is_active:
        return redirect('/login')
    return redirect('../../')