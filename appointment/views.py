import json

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from appointment.forms import BookingForm
from appointment.models import Appointment, BookAppointment
from product.models import User
from main.functions import generate_form_error


def index(request):
    appointment = Appointment.objects.all()
    context = {
        "title": "Pet shop | Appointment",
        "active" : "color-header",
        "all_appointments": True,
        "bg" : "active",
        "appointment": appointment,
    }

    return render(request, 'user/usr_appointment.html', context=context)  


@login_required(login_url="/user/login/")
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            if not User.objects.filter(user=request.user.is_anonymous):
                if not User.objects.filter(user=request.user).exists():
                    user = User.objects.create(user=request.user, name=request.user.username)
                else:
                    user = request.user.user

                instance = form.save(commit=False)
                instance.user = user
                instance.save()

                response_data ={
                    "title" : "Successfully Submitted",
                    "message" : "We will Contact you shortly",
                    "status" : "success",
                    # "redirect" : "yes",
                    # "redirect_url" : "/"
                }
                return HttpResponseRedirect(reverse("appointments:status"))
            else:
                response_data ={
                    "title" : "Not Logged In",
                    "message" : "You want to login For giving feedback",
                    "status" : "error",
                    "redirect" : "yes",
                    "redirect_url" : "/user/login/",
                }

                return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
            error_message = generate_form_error(form)

            response_data = {
                "title" : "From validation error",
                "message" : str(error_message),
                "status" : "error",
                "stable" : "yes",
            }
        return HttpResponse(json.dumps(response_data), content_type="application/json") 
    else:
        form = BookingForm()

        context ={
            "title": "Pet Shop | Contact-Us",
            "active" : "home",
            "contact" : True,
            "form": form,
        }

        return render(request, 'user/usr_Appointment_two.html', context=context)


@login_required(login_url="/user/login/")
def status(request):
    if not request.user.is_anonymous:
        user = request.user.user
    else:
        user=False

    status = BookAppointment.objects.filter(is_deleted=False, user=user).order_by('-id')

    context = {
        "title": "Pet shop | Appointment Status",
        "status_page": True,
        "bg" : "active",
        "status": status
    }

    return render(request, 'user/usr_appointment_status.html', context=context)  


@login_required(login_url="/user/login/")
def status_remove(request, pk):
    instance = get_object_or_404(BookAppointment, pk=pk)
    instance.is_deleted = True
    instance.save()

    response_data = {
        "title" : "Successfully Removed",
        "message" : "Appointment Removed successfully",
        "status" : "success",
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")