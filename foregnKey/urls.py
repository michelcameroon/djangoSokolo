from django.urls import path

from .views import ReporterListView, ArticleListView

urlpatterns = [
#    path('', views.index, name='index'),
    path('article', ArticleListView.as_view()),
    path('reporter', ReporterListView.as_view()), 
]

