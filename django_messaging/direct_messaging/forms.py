from django import forms


class MessageForm(forms.Form):
    username = forms.CharField(label="", max_length=100)
    message = forms.CharField(label="", max_length=1000)
