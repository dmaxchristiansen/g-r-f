from django.db import models
from apps.log_reg_app.models import User

class Project(models.Model):
    user = models.ForeignKey(User, related_name="projects")
    proj_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    desc = models.TextField()
    funds = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    proj_pic = models.FileField(upload_to='proj_pics/')
    url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    message = models.TextField()
    project = models.ForeignKey(Project, related_name="messages")
    user = models.ForeignKey(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
