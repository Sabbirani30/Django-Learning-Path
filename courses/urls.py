from django.urls import path
from. import views




urlpatterns = [
    
    path('', views.Sabbir ),
    path('course/', views.course),
    path('mahdi/', views.Mahdi_Sir),
    path('data_analysis/', views.Data_Analysis)
    
   ]