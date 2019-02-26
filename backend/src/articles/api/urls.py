from django.conf.urls import url

from .views import (ArticleListView, ArticleDetailView,ArticleCreateView)

urlpatterns = [
    url('',ArticleListView.as_view()),
    url('create/',ArticleCreateView.as_view()),
    url('<pk>',ArticleDetailView.as_view()),
]
