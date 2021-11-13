from django.urls import path
from .import views
urlpatterns = [
    path('insert/',views.insert, name = 'insert'),
    path('inputt/',views.inputt, name = 'inputt'),
    path('contacts/',views.contacts, name='contacts')
]