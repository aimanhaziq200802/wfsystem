from django.contrib import admin
from authentication.models import *
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_requester', 'is_verifier', 'is_approver', 'is_admin', 'is_final_approver', 'is_finance']
    list_editable = ['is_requester', 'is_verifier', 'is_approver', 'is_admin', 'is_final_approver', 'is_finance']
    list_filter = ['is_requester', 'is_verifier', 'is_approver', 'is_admin', 'is_final_approver', 'is_finance']
    search_fields = ['user__username']