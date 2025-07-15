from django.urls import include, path
from project import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/',views.add, name='add'),
    path('<book_id>/edit/',views.edit, name='edit'),
    path('<blog_id>/delete/',views.delete, name='delete'),
]
