from django import forms

from appointment.models import BookAppointment



class BookingForm(forms.ModelForm):

    class Meta:
        model = BookAppointment
        exclude = ('user', 'status', 'note', 'is_deleted')

        widgets = {
            "contact_number" : forms.TextInput(attrs={'placeholder': 'Enter your contact number', 'value': '+91'}),
        }
