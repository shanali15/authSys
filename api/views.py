from django.http import JsonResponse
from django.http import HttpResponse
import json

def api_home(request, *args, **kwargas):
    body = request.body
    data = {}
    try:
        data= json.load(body)
    except:
        print("unable to load",body)
    print(body)
    return JsonResponse(data)
    # return HttpResponse("This is the response")