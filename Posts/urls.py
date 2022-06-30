from django.urls import path

from . import views

urlpatterns = [
    path('newpost/', views.newpost, name='newpost'),
    path('view_post/<slug>', views.view_post, name='view_post'),
    path('edit_post/<slug>', views.edit_post, name='edit_post'),
    path('delete_post/<slug>', views.delete_post, name='delete_post'),
    path("newpost/", views.newpost, name="newpost"),
]