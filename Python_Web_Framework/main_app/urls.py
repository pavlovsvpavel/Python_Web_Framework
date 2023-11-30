from django.urls import path

from Python_Web_Framework.main_app import views

urlpatterns = (
    path('', views.index, name='index'),
)
