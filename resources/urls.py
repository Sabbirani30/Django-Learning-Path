from django.urls import path
from . import views

urlpatterns = [
    

   
    path('bio/', views.Biology), 
    path('math/', views.Math),
    path('phy/', views.Physics),
    path('chem/', views.Chemistry),
    path('bd/', views.Big_Data),
    
   ]