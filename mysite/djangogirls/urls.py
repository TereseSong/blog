from django.urls import path
from . import views

app_name = 'djangogirls'

urlpatterns = [
    path('',views.index,name='index'),
    path('hello/', views.hello_world, name='hello'),
    path('home/',views.home,name='home'),
    path('post/<int:id>/', views.post_detail,
         name='post/<int:id>'),
]

