from django.db import models
from django.utils import timezone
from django.conf import settings

class Brand(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='brands')  # Foreign key to User model

    logo = models.ImageField(upload_to='brands/logos/', blank=True, null=True)  # Optional logo field
    brand_name = models.CharField(max_length=255)
    owner_full_name = models.CharField(max_length=255)
    account_creation_date = models.DateField(default=timezone.now)  # Automatically set to today's date
    phone_number = models.CharField(max_length=15)  # Adjust max_length based on your needs
    email_id = models.EmailField()
    gstin_number = models.CharField(max_length=15)  # Adjust max_length based on your GSTIN format

    # Bank details
    bank_account_number = models.CharField(max_length=20)  # Adjust based on your requirements
    ifsc_code = models.CharField(max_length=11)  # IFSC codes are usually 11 characters long
    bank_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.brand_name} ({self.owner_full_name})"

# Create your models here.
