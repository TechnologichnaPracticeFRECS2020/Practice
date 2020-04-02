from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserRequest(models.Model):
    type = models.IntegerField()
    result = models.TextField()
    request_time = models.DateTimeField(default=timezone.now)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.result
