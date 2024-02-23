import hashlib
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.registration.views import VerifyEmailView,RegisterView
from allauth.account import signals
from allauth.account.adapter import get_adapter
from django.core.exceptions import ObjectDoesNotExist
from .serializers import CustomRegisterSerializer,CustomVerifyEmailSerializer
from .models import Otp
from django.urls import reverse_lazy



class verify_otp_mail(VerifyEmailView):
    
    def get_serializer(self, *args, **kwargs):
        return CustomVerifyEmailSerializer(*args, **kwargs)

    def post(self, request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        request_otp = request.data.get('otp')
        hashed_request_otp =  hashlib.sha256(request_otp.encode()).hexdigest()
        try : 
            otp_obj = Otp.objects.get(otp=hashed_request_otp)
            email_address = otp_obj.email
            
            expired = otp_obj.expired
            if not expired : 
                if not email_address.verified:
                    request.user.verified = True
                    confirmed = get_adapter().confirm_email(request, email_address)
                if email_address.verified:
                    signals.email_confirmed.send(
                        sender=self.__class__,
                        request=request,
                        email_address=email_address,
                    )
                return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
            return Response({'message':"otp expired please resend the verification email"},status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_response_data(user)
        
        confirmation_url = reverse_lazy('account_otp_verification_sent')
        redirect_url = f"{confirmation_url}?email={user.email}"
        data['success_url'] = redirect_url
        if data:
            response = Response(
                data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

        return response