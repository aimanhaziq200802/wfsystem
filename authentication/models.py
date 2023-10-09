from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_requester = models.BooleanField(default=False)
    is_verifier = models.BooleanField(default=False)
    is_approver = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_final_approver = models.BooleanField(default=False)
    is_finance = models.BooleanField(default=False)


