from django.urls import path, include,re_path
from posts import views


app_name = "posts"

urlpatterns = [
    path('create/', views.create_event, name="create_post"),
    path('edit/<uuid:pk>/', views.edit_event, name="edit_event"),
    path('delete/<uuid:pk>/', views.delete_event, name='delete_event'),
]
