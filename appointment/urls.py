from django.urls import path
from appointment import views


app_name = "appointments"


urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking, name='booking'),
    path('status/', views.status, name='status'),
    path('status/remove/<int:pk>', views.status_remove, name='status_remove'),
]