from django.db import models
from .enums import userType

from django.contrib.auth.models import AbstractUser
# Create your models here

class User(AbstractUser):
    account_type = models.CharField(choices=userType.choices(), default=userType.CUSTOMER)
    password = models.CharField(min_length=8, max_length=16, required=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'email', 'password', 'account_type']

    def _get_user_name(self) -> str:
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    def __str__(self) -> str:
        return 'Account created for {} successfully'.format(self._get_user_name())