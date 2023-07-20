
from django.contrib import admin
from django.urls import path
from app.views import index, add_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add_student/', add_student, name='add_student'),
]
