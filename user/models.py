from django.db import models
from django.core.validators import RegexValidator

class UserProfile(models.Model):
    username = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Enter a valid username. This value may contain only letters, digits, and @/./+/-/_ characters.',
                code='invalid_username'
            )
        ]
    )
