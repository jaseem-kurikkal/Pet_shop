from django.contrib import admin

from appointment.models import Appointment, BookAppointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "doc_name", "days")

admin.site.register(Appointment, AppointmentAdmin)


class BookAppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(BookAppointment, BookAppointmentAdmin)
