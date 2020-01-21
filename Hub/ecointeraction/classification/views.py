from django.http import HttpResponse
from django.shortcuts import render
from .models import Entity, Criterium, Characteristic, InteractiveSystem

# $( "#application" ).append("<div class='col s3' id='"+id+"'><div class='card small'><div class='card-image'><a href='"+ref+"'><img src='"+img+"'><span class='card-title'>"+application["name"]+"</span></a></div></div></div>");
def classification(request):
    #return HttpResponse("Done.")
    interactive_systems = InteractiveSystem.objects.order_by('name')
    entities = Entity.objects.all()
    criteria = Criterium.objects.all()
    characteristics = Characteristic.objects.all()
    return render(request, 'classification/classification.html', locals())


def interactive_system(request, interactive_system_id):
	interactive_system = InteractiveSystem.objects.get(id=interactive_system_id)
	return render(request, 'classification/interactive_system.html', interactive_system)