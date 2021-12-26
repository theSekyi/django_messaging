from django.shortcuts import render
from .forms import MessageForm
from .models import MessageModel

# from django.contrib.auth.decorators import login_required


# Create your views here.
def inbox(request):
    user = request.user
    messages = MessageModel.get_messages(user=user)
    active_direct = None
