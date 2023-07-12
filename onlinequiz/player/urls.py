from django.urls import path
from .views import *




urlpatterns = [   
               
  path('home',quizhome,name='Home'),
  path('scilevel',sci_level,name='Slevel'),
  path('histlevel',hist_level,name='Hlevel'),
  path('scil1',sl1,name='Sl1'),
  path('questions', display_questions, name='ds'),
  path('questions2',sciencel2, name='sds2'),
  path('questions3',sciencel3, name='sds3'),
  path('history1',historyl1, name='h1'),
  path('history2',historyl2, name='h2'),
  path('history3',historyl3, name='h3'),
  path('score/<int:score>/', display_score, name='score'),  

]