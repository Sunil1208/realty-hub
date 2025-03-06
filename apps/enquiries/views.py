from django.core.mail import send_mail

from real_estate.settings.development import DEFAULT_FROM_EMAIL
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.enquiries.models import Enquiry

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        receipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=receipient_list, fail_silently=True)

        enquiry = Enquiry.objects.create(
            name=name,
            email=email,
            message=message
        )
        enquiry.save()

        return Response({"success": "Your Enquiry was successfully submitted."})
    except Exception as e:
        return Response({"fail": "An error occurred while sending your enquiry."})
