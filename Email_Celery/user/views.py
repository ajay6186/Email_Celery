from django.shortcuts import render
from .models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


@csrf_exempt
def get_user_data(request):
    try:
        reponse = list()
        if request.GET.get('id'):
            datas = User.objects.get(id=request.GET.get('id'))
            response_data = {}
            response_data['id'] = datas.id
            response_data['first_name'] = datas.first_name
            response_data['last_name'] = datas.last_name
            response_data['mobile'] = datas.mobile
            response_data['email'] = datas.email
            response_data['password'] = datas.password
            return JsonResponse({'data': response_data})
        else:
            datas = User.objects.all()

        if datas:
            for data in datas:
                response_data = {}
                response_data['id'] = data.id
                response_data['first_name'] = data.first_name
                response_data['last_name'] = data.last_name
                response_data['mobile'] = data.mobile
                response_data['email'] = data.email
                response_data['password'] = data.password
                if response_data:
                    reponse.append(response_data)
        else:
            reponse = {
                'message': 'Not find any user'
            }
        print(datas)
    except User.DoesNotExist:
        reponse = {
            'status': 200,
            'message': 'please give the vailid user id'
        }
    except:
        reponse = {
            'status': 400,
            'message': 'Error something Wrong'
        }
    return JsonResponse({'data': reponse})
