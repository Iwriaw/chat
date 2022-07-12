from django.db import models
from datetime import datetime, timezone
from user.models import User


class Chatroom(models.Model):
    '''
    User Model
    '''
    name = models.CharField(max_length=64)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(
        default=datetime.utcnow)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['creator'])
        ]


class ChatRecord(models.Model):
    '''
    Chat Record
    '''
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    send_time = models.DateTimeField(
        default=datetime.utcnow)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['chatroom']),
            models.Index(fields=['send_time'])
        ]
