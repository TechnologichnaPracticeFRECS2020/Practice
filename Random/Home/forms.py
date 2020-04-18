from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import UserRequest

        
        
class RequestForm(forms.ModelForm):
    
    class Meta:
        model = UserRequest
        fields = ['type', 'result', 'request_time', 'requester']


