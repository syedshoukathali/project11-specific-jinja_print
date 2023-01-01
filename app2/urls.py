from django.urls import path
from app2.views import *




app_name='indraa'

urlpatterns=[
    path('indra/',indra,name='indra'),
  ]