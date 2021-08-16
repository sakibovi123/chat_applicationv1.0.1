from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ChatRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    
    def __str__(self):
        return str(self.user)
    
class ReplyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField()
    
    
    def __str__(self):
        return str(self.user)



