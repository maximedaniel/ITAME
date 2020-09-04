from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'sedyl/index.html')

@csrf_exempt
def script(request):
    if request.method == 'GET':
        return HttpResponse("ERROR")

    elif request.method == 'POST':
        print(request.body)
        return HttpResponse("OK")