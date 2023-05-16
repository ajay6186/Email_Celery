from django.shortcuts import render
from .models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def get_user_data(request):
    reponse = {}
    datas = User.objects.all()
    for data in datas:
        reponse['first_name'] = data.first_name
        reponse['last_name'] = data.last_name
        reponse['mobile'] = data.mobile
        reponse['email'] = data.email
    return JsonResponse(reponse)