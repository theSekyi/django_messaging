from django.db import models
from django.contrib.auth import get_user_model
from datetime import timezone
from django.db.models import Max

# Create your models here.

User = get_user_model()


class BaseModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Set this model as Abstract


# class MessageThreadModel(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
#     has_unread = models.BooleanField(default=False)


class MessageModel(BaseModel):
    # thread = models.ForeignKey("MessageThreadModel", related_name="+", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="", blank=True, null=True)
    is_read = models.BooleanField(default=False)

    def send_message(sender, receiver, body):
        sender_message = MessageModel(user=sender, sender=sender, recipient=receiver, body=body, is_read=True)
        sender_message.save()

        recipient_message = MessageModel(user=receiver, sender=sender, body=body, recipient=receiver)
        recipient_message.save()

        return sender_message

    def get_messages(user):
        users = []

        messages = (
            MessageModel.objects.filter(user=user)
            .values("recipient")
            .annotate(last=Max("created_on"))
            .order_by("-last")
        )

        for message in messages:
            users.append(
                {
                    "user": User.objects.get(pk=message["recipient"]),
                    "last": message["last"],
                    "unread": MessageModel.objects.filter(
                        user=user, recipient__pk=message["recipient"], is_read=False
                    ).count(),
                }
            )
        return users
