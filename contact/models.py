from django.db import models

# Create your models here.

class message(models.Model):
    from_email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=30, null=False, blank=False)
    message = models.TextField(max_length=300,null=False, blank=False)

    def __str__(self):
        return self.subject