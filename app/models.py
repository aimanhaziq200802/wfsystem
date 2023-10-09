import os
from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    
class Entity(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Quotation(models.Model):
    STATUS_CHOICES_VERIFIER = (
        ("PENDING", "pending"),
        ("VERIFIED", "verified"),
        ("REJECTED", "rejected"),
    )

    STATUS_CHOICES_APPROVER = (
        ("PENDING", "pending"),
        ("APPROVED", "approved"),
        ("REJECTED", "rejected"),
    )

    FINAL_APPROVER_STATUS_CHOICES = (
        ("PENDING", "pending"),
        ("APPROVED", "approved"),
        ("REJECTED", "rejected"),
    )

    FINANCE_STATUS_CHOICES = (
        ("PENDING", "pending"),
        ("APPROVED", "approved"),
        ("REJECTED", "rejected"),
    )


    qid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='initiated_quotations', blank=True)
    remarks = models.TextField(null=True, blank=True)
    # attachment = models.FileField(upload_to='quotations_attachments/', null=True, blank=True)

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='quotations')
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, related_name='quotations')
    entity = models.ForeignKey(Entity, on_delete=models.SET_NULL, null=True, related_name='quotations')
    supplier = models.CharField(max_length=255, null=True)
    item = models.CharField(max_length=255, null=True)
    specification = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    verifier = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='verified_quotations', null=True, blank=True)
    verify_status = models.CharField(default='pending', choices=STATUS_CHOICES_VERIFIER, max_length=20)
    verified_at = models.DateTimeField(null=True, blank=True)    
    verify_remarks = models.CharField(max_length=50, blank=True, null=True, help_text="Max length is 50 characters")

    approver = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='approved_quotations', null=True, blank=True)
    approve_status = models.CharField(default='pending', choices=STATUS_CHOICES_APPROVER, max_length=20, blank=True, null=True)
    approval_at = models.DateTimeField(null=True, blank=True)
    approval_remarks = models.CharField(max_length=50, blank=True, null=True, help_text="Max length is 50 characters")

    final_approver = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='final_approved_quotations', null=True, blank=True)
    final_approval_status = models.CharField(default='PENDING', choices=FINAL_APPROVER_STATUS_CHOICES, max_length=20, blank=True, null=True)
    final_approval_at = models.DateTimeField(null=True, blank=True)
    final_approval_remarks = models.CharField(max_length=50, blank=True, null=True)

    finance_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='finance_user_quotations', null=True, blank=True)
    finance_status = models.CharField(default='PENDING', choices=FINANCE_STATUS_CHOICES, max_length=20, blank=True, null=True)
    finance_reviewed_at = models.DateTimeField(null=True, blank=True)    
    finance_remarks = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.qid)
    

class QuotationAttachment(models.Model):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='quotations_attachments/', blank=True, null=True)
    
    def filename(self):
        return os.path.basename(self.file.name)

