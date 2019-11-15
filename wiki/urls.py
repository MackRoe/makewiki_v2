from django.urls import path
from wiki.views import PageListView, PageDetailView, PageAddcardView


urlpatterns = [
    path('addcard/', PageAddcardView.as_view(), name='addcard'),
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
