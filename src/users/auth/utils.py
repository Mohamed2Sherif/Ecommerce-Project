import os
import random
import hashlib
from .models import Otp
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist

def generate_otp(email,length=6):
    """
    Generate a cryptographically secure random OTP (One-Time Password) of the specified length.
    
    Parameters:
        length (int): The length of the OTP. Default is 6.
    
    Returns:
        str: The generated OTP.
    """
    digits = "0123456789"
    otp = ''.join(random.choice(digits) for _ in range(length))
    expiration_time = timezone.now() + timedelta(minutes=settings.OTP_EXPIRE_AFTER)
    hashed_otp = hashlib.sha256(otp.encode()).hexdigest()  # Hash the OTP
    otp_obj = Otp(otp=hashed_otp,email=email ,valid_untill=expiration_time)
    try :
        update_existing_otp = Otp.objects.get(email=email)
        update_existing_otp.otp = otp_obj.otp
        update_existing_otp.valid_untill = otp_obj.valid_untill
        update_existing_otp.save()
    except ObjectDoesNotExist:
        otp_obj.save()
    return otp

@shared_task
def delete_expired_otps():
    expired_otps = Otp.objects.filter(valid_until__lt=timezone.now())
    expired_otps.delete()
