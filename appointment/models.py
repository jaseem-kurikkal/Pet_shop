from django.db import models

from product.models import User
from phonenumber_field.modelfields import PhoneNumberField


STATUS = (
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected'),
    ('Accepted', 'Accepted'),
)


class Appointment(models.Model):
    image = models.FileField(upload_to="appointment/")
    doc_name = models.CharField(max_length=100)
    days = models.CharField(max_length=150)
    added_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.doc_name
    

class BookAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doc_name = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = PhoneNumberField()
    category = models.ForeignKey("product.Category", on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, null=True, blank=True)
    note = models.CharField(max_length=100, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


