from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('teachers/',views.teachers,name='teachers'),
    path('teachers/<str:name>',views.teacher,name='teacher')
]
