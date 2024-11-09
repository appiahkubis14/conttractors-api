from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Custom user model for contractors
class Contractor(AbstractUser):
    full_name = models.CharField(max_length=100)
    
    # Set unique related_name attributes to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="contractor_groups",
        blank=True,
        help_text="The groups this contractor belongs to.",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="contractor_permissions",
        blank=True,
        help_text="Specific permissions for this contractor.",
    )

# Model for farmer details
class Farmer(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    photo = models.ImageField(upload_to='farmers/photos/' , blank=True)

