from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from core.models import Country

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    country = models.ForeignKey(Country,on_delete=models.CASCADE,blank=True,null=True)

    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)


    privacy_policy =models.BooleanField(default=False)
    token =models.CharField(max_length=120)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    @property
    def full_phone_number(self):
        if self.country:
            if self.country.phone_code:
                return f"{self.country.phone_code} {self.phone_number}"
            else:
                return f"Null {self.phone_number}"
        else:
            return f"Null {self.phone_number}"
 



    
