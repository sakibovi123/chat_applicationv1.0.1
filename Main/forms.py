from django import forms
from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = '__all__'
        

class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyModel
        fields = '__all__'