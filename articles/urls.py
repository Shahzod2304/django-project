
























#Photoni joylashtirib olgach.
from django.urls import path
from .views import (
    ArticlesListView,
    ArticlesUpdateView,
    ArticlesDeleteView,
    ArticlesDetailView,
    ArticleCreateView,
)
urlpatterns = [
    path('<int:pk>/edit/', ArticlesUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticlesDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticlesDeleteView.as_view(), name='article_delete'),
    path('',ArticlesListView.as_view(), name='article_list'),

    path('new/',ArticleCreateView.as_view(), name='article_new'),

]
