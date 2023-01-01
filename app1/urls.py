from django.urls import path
from app1.views import *

app_name='shoukath'

urlpatterns=[
    path('shoukathalikhan/',shoukathalikhan,name='shoukathalikhan'),
]