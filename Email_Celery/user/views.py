from django.shortcuts import render
from .models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.mail import send_mail
import json
import smtplib
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import random


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

# send data in params


@csrf_exempt
def create_user_account(request):
    if request.method == "POST":
        first_name = request.GET.get('firstName')
        last_name = request.GET.get('lastName')
        email = request.GET.get('email')
        mobile = request.GET.get('mobile')
        address = request.GET.get('address')
        password = request.GET.get('password')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            address=address,
            password=password
        )
        # send_email = send_otp_email()

        subject = 'welcome to Django World'
        message = f"<h1>Hi {first_name} {last_name}, thank you for registering in Django World.</h1>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        data = send_mail(subject, message, email_from, recipient_list)
        return JsonResponse({"message": "send_email"})


@csrf_exempt
def create_user_account_body(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data)
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        mobile = data.get('mobile')
        address = data.get('address')
        password = data.get('password')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            address=address,
            password=password
        )

        subject = 'welcome to Django World otp'
        message = f"<h1>Hi {first_name} + {last_name}, thank you for registering in Django World.</h1>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        data = send_mail(subject, message, email_from, recipient_list)
        return JsonResponse({"message": "Thanks for registration otp has been send"})
