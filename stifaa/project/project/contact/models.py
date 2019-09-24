
from django.db import models
from django.utils import timezone
from django.conf import settings



class NewsletterUser(models.Model):
    email=models.EmailField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# class User(models.Model):
#     email=models.EmailField()
#     date_added=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.emai