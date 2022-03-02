from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.payment_list, name='list'),
    path('<int:pk>', views.payment_detail, name='details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
