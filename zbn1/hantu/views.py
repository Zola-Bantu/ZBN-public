from django.shortcuts import render

# Create your views here.

def sitemap(request):
    context = {
	
    }
    template = 'muntu/map.html'
    return render(request, template, context)
