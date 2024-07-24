from django.db import models
import uuid

# Create your models here.
class Mail(models.Model):
    uid = models.UUIDField(default=uuid.uuid4)
    email = models.EmailField()
    subject = models.CharField(max_length=40, default="New Inquiry")

    def __str__(self):
        return str(self.uid)