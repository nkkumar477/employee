from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'emp', views.emp, name='index'),
    path(r'show', views.show, name='show'),
    path(r'edit/<int:id>', views.edit, name='edit'),
    path(r'update/<int:id>', views.update, name='update'),
    path(r'delete/<int:id>', views.destroy, name='delete'),
]
