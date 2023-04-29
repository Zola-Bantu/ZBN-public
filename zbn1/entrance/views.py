from django.shortcuts import render
from .utils  import Challenge
from .models import Qrcode
# Create your views here.

def secure(request):
    chal = Challenge()
    name = chal.generate() 
    qrcode = Qrcode.objects.create(
        name = name , 
        path = 'entrance/static/entrance/image/' ,
    )
    context = {
    	"name": name + ".png"
    }
    template = 'entrance/monyako.html'
    return render(request, template, context)
