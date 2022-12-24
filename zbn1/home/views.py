from django.shortcuts import render

# Create your views here.

def monyako(request):
    
    context = {}
    template = 'home/monyako.html'
    return render(request, template, context)