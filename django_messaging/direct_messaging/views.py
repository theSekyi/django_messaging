from django.shortcuts import render
from .forms import MessageForm
from .models import MessageModel
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def inbox(request):
    user = request.user
    messages = MessageModel.get_messages(user=user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message["user"].username
        directs = MessageModel.objects.filter(user=user, recipient=message["user"])
        directs.update(is_read=True)

        for message in messages:
            if message["user"].username == active_direct:
                message["unread"] = 0

    context = {"directs": directs, "messages": messages, "active_direct": active_direct}

    template = loader.get_template("direct_messaging/inbox.html")
    return HttpResponse(template.render(context, request))
