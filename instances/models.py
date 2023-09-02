from django.db import models
from .enums import userType

from django.contrib.auth.models import AbstractUser
# Create your models here

class User(AbstractUser):
    name = models.CharField(blank=True, max_length=32)
    email = models.EmailField(unique=True, db_index=True)
    account_type = models.CharField(choices=userType.choices(), default=userType.CUSTOMER, max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['name', 'email', 'account_type']

    def _get_user_name(self) -> str:
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    def __str__(self) -> str:
        return 'Account created for {} successfully'.format(self._get_user_name())