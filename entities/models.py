from django.db import models
from django.contrib.auth.models import User

class Entity(models.Model):
  name = models.CharField(max_length=100)
  address = models.TextField()
  phones = models.ForeignKey('phones.Phones', blank=True, null=True)
  email = models.ForeignKey('emails.Email', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ManyToManyField(User)
  last_modified_at = models.DateTimeField(auto_now=True)
  last_modified_by = models.ManyToManyField(User)
  is_active = models.BooleanField(default=True)
