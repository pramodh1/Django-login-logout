from django.urls import path
from . import views
urlpatterns = [
    path('registration',views.registration,name='registration'),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),

]