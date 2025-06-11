
from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('host/', views.host_game, name='host'),
    path('join/', views.join_game, name='join'),
    path('get_question/', views.get_question, name='get_question'),
    path('check_answer/', views.check_answer, name='check_answer'),
]
