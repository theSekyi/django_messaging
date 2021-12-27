from django.shortcuts import render
from .forms import MessageForm
from .models import MessageModel

# from django.contrib.auth.decorators import login_required


# Create your views here.
def inbox(request):
    user = request.user
    messages = MessageModel.get_messages(user=user)
    active_direct = None
    directs = None
    directs.update(is_read=True)

    for message in messages:
        if message["user"].username == active_direct:
            message["unread"] = 0

    context = {"directs": directs, "messages": messages, "active_direct": active_direct}

    # template = loader.get_template("direct_messaginf/inbox.html")
    # return HttpResponse(template.render(context, request))
