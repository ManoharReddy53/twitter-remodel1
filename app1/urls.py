from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.feed,name="home"),
    path('login',views.loginView,name="login"),
    path('register',views.register,name='register'),
    path('post',views.postView,name='post'),
    path('profile',views.profile,name='profile'),
    path('logout/cdk',views.logoutView,name='logout'),
    path('delete/<int:rid>',views.Delete,name="delete"),
    path('view/<int:rid>',views.view,name="view")
]