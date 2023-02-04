from django.shortcuts import render
from .utils import Challenge
# Create your views here.

def monyako(request):
    chal = Challenge()
    name = chal.generate()
    context = {
    	"name": name + ".png"
    }
    template = 'muntu/monyako.html'
    return render(request, template, context)
