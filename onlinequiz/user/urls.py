from django.urls import path
from .views import *



urlpatterns = [
   
    path('register',Regview.as_view(),name='regv'),
    path("lgout",Lgout.as_view(),name='logout'),
  

]