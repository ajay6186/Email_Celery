from django.conf import settings


def registration_email(first_name, last_name):
    subject = 'welcome to Django World'
    message = f"Hi {first_name} + {last_name}, thank you for registering in Django World."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email,]
    data = send_mail(subject, message, email_from, recipient_list)
    return JsonResponse({"message": "Thanks for registration"})
