from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from hantu.signals import page_viewed_signal
from hantu.utils import get_client_ip, get_info
#from hantu0.utils Challenge
#from kuntu.meroetic import meroetic, meroe_preview
#from kuntu.proverbs import proverbs
from allauth.account.models import EmailAddress
from django.urls import reverse

import logging, os, time, calendar, datetime

name = "BlackMail"

# Create and configure logger
if 'logs' not in os.listdir('.'):
    os.mkdir('logs')  # Create directory called logs
    
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s - %(funcName)s"
logging.basicConfig(
    filename = "logs/main.Log",
    level = logging.DEBUG,
    format = LOG_FORMAT
    )
logger = logging.getLogger()


def choose():
    length = len(proverbs)
    number = int(time.time()) % length
    return number



def sitemap(request):
    
    status, country, country_code, region_code, region, town, zip_code, lat, lon, timezone, isp, organization, az, query = get_info(get_client_ip(request))
    
    #prov = proverbs[choose()]
    url = request.path
    #print(url)
    
    context = {
    	#'proverb': prov["phrase"],
    	#'reference': prov["reference"],
    	'year': "%s" % (datetime.date.today().year),
    	'time': time.strftime("%H:%M:%S"),
    	#'meroetic': lis,
    	'url': url,
    	'country': country,
    	'ccode': country_code,
    	'region': region,
    	'rcode': region_code,
    	'town': town, 
    	'zip_code': zip_code,
    	'lat': lat, 
    	'lon': lon, 
    	'timezone': timezone, 
    	'isp': isp, 
    	'organization': organization,
    	'az': az, 
    	'qwery': query,
	
    }
    template = 'muntu/map.html'
    return render(request, template, context)

def chat(request):
    
    status, country, country_code, region_code, region, town, zip_code, lat, lon, timezone, isp, organization, az, query = get_info(get_client_ip(request))
    
    context = {
	
    }
    template = 'muntu/chat.html'
    return render(request, template, context)


