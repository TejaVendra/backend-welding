from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WorkImage
from .serializer import WorkImageSerializer
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import DesignOrder
import json
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags



class WorkImagesByCategory(APIView):
    def get(self, request, category):
        images = WorkImage.objects.filter(category=category)
        serializer = WorkImageSerializer(images, many=True)
        return Response(serializer.data)

# views.py

# designs/views.py



@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        order = DesignOrder.objects.create(
            name=data['name'],
            village=data['village'],
            phone=data['phone'],
            design_name=data['design_name'],
        )

        # Send Email Notification
        subject = f"New Design Order - {order.design_name}"

        html_content = f"""
        <h2 style="color: #2c3e50;">🚀 New Design Order Received!</h2>
        <ul style="font-size: 16px;">
        <li><strong>Design:</strong> {order.design_name}</li>
        <li><strong>Name:</strong> {order.name}</li>
        <li><strong>Village:</strong> {order.village}</li>
        <li><strong>Phone:</strong> {order.phone}</li>
        <li><strong>Time:</strong> {order.submitted_at.strftime('%Y-%m-%d %H:%M:%S')}</li>
        </ul>
        <p style="color: #16a085;">Please follow up with the customer.</p>
        """

        text_content = strip_tags(html_content)  # fallback plain text

        email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [settings.EMAIL_RECEIVER])
        email.attach_alternative(html_content, "text/html")
        email.send()


        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'invalid request'}, status=400)
