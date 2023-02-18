from django.shortcuts import render
from .utils import Challenge
# Create your views here.

def secure(request):
    chal = Challenge()
    name = chal.generate()
    context = {
    	"name": name + ".png"
    }
    template = 'entrance/monyako.html'
    return render(request, template, context)
