from django.urls import path

from .views import Table1ListView

urlpatterns = [
#    path('', views.index, name='index'),
    path('list', Table1ListView.as_view()), 
]

