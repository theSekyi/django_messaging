from django.shortcuts import render
from .forms import MessageForm
from .models import MessageModel
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

User = get_user_model()

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


@login_required
def search_users_to_dm(request):
    query = request.GET.get("q")
    users_paginator = None

    if query:
        users = User.objects.filter(Q(username__icontains=query))

        paginator = Paginator(users, 5)
        page_number = request.GET.get("page")
        users_paginator = paginator.get_page(page_number)

    context = {"users": users_paginator}

    return render(request, "direct_messaging/search_users.html", context)
