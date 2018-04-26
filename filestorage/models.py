from django.db import models
from django.contrib.auth.models import User
import uuid

def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.id, str(uuid.uuid4()))

class UserFile(models.Model):
    description = models.CharField(max_length=1024)
    file = models.FileField(upload_to=user_directory_path)
    file_name = models.CharField(max_length=1024, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)