from datetime import datetime

from django.shortcuts import render
from .models import Device
# Create your views here.

from django.http import HttpResponse
# decorador para evitar errores de interdomain
from django.views.decorators.csrf import csrf_exempt
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


@csrf_exempt
def login_router(request):
    mac=request.POST.get('mac')
    ip = request.POST.get('ip')
    linklogin = request.POST.get('link-login')
    linkorig = request.POST.get('link-orig')
    linkloginonly = request.POST.get('link-login-only')
    chapid = request.POST.get('chap-id')
    chapchallenge = request.POST.get('chap-challenge')
    error = request.POST.get('error')
    linkorigesc = request.POST.get('link-orig-esc')
    macesc = request.POST.get('mac-esc')
    serveraddress = request.POST.get('server-address')
    servername = request.POST.get('server-name')
    trial = request.POST.get('trial')


    data = {"mac" : mac ,
            "ip" : ip,
            "error": error,
            "trial": trial,
            "macesc": macesc,
            "linkorigesc": linkorigesc,
            "linklogin" : linklogin,
            "linkorig" : linkorig,
            "chapid": chapid,
            "chapchallenge": chapchallenge,
            "linkloginonly": linkloginonly,
            "servername": servername,
            "serveraddress": serveraddress
            }

    return render(request,'portal/login.html', data)

@csrf_exempt
def save_device(request):
    mac=request.POST.get('mac')
    ip = request.POST.get('ip')
    error = request.POST.get('error')
    macesc = request.POST.get('mac-esc')
    serveraddress = request.POST.get('server-address')
    servername = request.POST.get('server-name')
    trial = request.POST.get('trial')
    username = request.POST.get('username')
    loggedin = request.POST.get('logged-in')

    device = Device.objects.filter(mac=mac).first()
    
    if not device:
        device = Device()

    device.mac = mac
    device.ip = ip
    device.hotspot = servername
    device.logged_in = False if loggedin=='no' else True
    device.last_login = datetime.now()
    device.account = username
    device.save()
    logger.info(device)

    data = {"mac" : mac ,
            "ip" : ip,
            "error": error,
            "trial": trial,
            "macesc": macesc,
            "username": username,
            "servername": servername,
            "serveraddress": serveraddress,
            "loggedin": loggedin
            }

    return render(request,'portal/device-info.html', data)

def disconnect_device(request, mac):

    device = Device.objects.filter(mac=mac).first()
    logger.info(device.mac)
    if device :
        device.logged_in = False
        device.save()
        logger.info(device.logged_in)

    return HttpResponse(f'user with mac {mac} disconnect')
