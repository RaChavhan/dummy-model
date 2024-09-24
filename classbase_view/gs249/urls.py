
from django.urls import path
from . import views
 
urlpatterns = [
    
    path('func',views.myview, name='myview'),
    path('class/', views.CLbaseView.as_view(name="Vaibhav"), name='CLbaseView') # it will take name=vaibhav
]