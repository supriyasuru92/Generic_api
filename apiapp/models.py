from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (

    ('Manager', 'Manager'),
    ('Employee', 'Employee'),
    ('Client', 'Client'),
)

CHOICES = (

    ('Pending', 'Pending'),
    ('Complete', 'Complete'),

)


class MyUser(AbstractUser):
    roles = models.CharField(max_length=50, choices=ROLES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Task(models.Model):
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    task_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=50, choices=CHOICES, default='Pending')
