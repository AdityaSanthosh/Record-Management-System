from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newentry/', views.newentry, name='newentry'),
    # path('newentry/', views.CreateNewEntry.as_view(), name='newentry'),
    path('deleteentry/<int:entryid>/', views.delete_entry, name='deleteentry'),
    path('updateentry/<int:entryid>/', views.update_entry, name='updateentry'),
    path('searchresult/', views.searchresult, name='searchresult'),
    path('indexing/', views.indexentries, name='indexing')
]
