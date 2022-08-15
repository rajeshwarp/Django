from django.urls import path
from .views import rental_review,thank_you

app_name = 'cars'

urlpatterns = [
    path('rental_review/',rental_review, name='rental_review'),
    path('thank_you/',thank_you, name='thank_you'),
]
