from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class BaseModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Set this model as Abstract


class MessageThreadModel(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    has_unread = models.BooleanField(default=False)


class MessageModel(BaseModel):
    thread = models.ForeignKey("MessageThreadModel", related_name="+", on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="", blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
