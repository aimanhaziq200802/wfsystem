from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from app.models import Quotation


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'})
    )

class LoginView(LoginView):
    template_name = 'login.html'

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        error_messages={
            'required': 'Please enter your username.',
        },
        widget=forms.TextInput(attrs={
            'class': 'my-custom-class',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        error_messages={
            'required': 'Please enter your password.',
        },
        widget=forms.PasswordInput(attrs={
            'class': 'my-custom-class',
            'placeholder': 'Password'
        })
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Incorrect username or password.",
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


def queue_counter(request):
    # Count quotations awaiting verification and assigned to the logged-in user as verifier
    quotations_awaiting_verification = Quotation.objects.filter(
        verify_status="PENDING", 
        verifier=request.user
    ).count()

    # Count quotations awaiting approval and assigned to the logged-in user as approver
    quotations_awaiting_approval = Quotation.objects.filter(
        approve_status="PENDING", 
        approver=request.user
    ).count()

    quotations_awaiting_final_approval = Quotation.objects.filter(
        final_approval_status="PENDING", 
        final_approver=request.user
    ).count()

    quotations_awaiting_finance_approval = Quotation.objects.filter(
        finance_status="PENDING", 
        finance_user=request.user
    ).count()  



    context = {
        # ... your other context data ...
        'quotations_awaiting_verification': quotations_awaiting_verification,
        'quotations_awaiting_approval': quotations_awaiting_approval,
        'quotations_awaiting_final_approval' : quotations_awaiting_final_approval,
        'quotations_awaiting_finance_approval' : quotations_awaiting_finance_approval
    }

    return render(request, 'home.html', context)

