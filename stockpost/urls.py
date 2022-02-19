from django.urls import path
from . import views, views2

urlpatterns = [
    path('', views.index, name="Index"),
    path('content/<str:slug>', views.content, name="content"),

    path('search/', views.search, name="search"),
    path('addContent/', views.addContent, name="addContent"),
    path('contact/', views.contact, name="contact"),
    path('vc/', views.validateContact, name="validateContact"),
    path('validate/', views.validate, name="validate"),
    path('signup/', views2.handleSignup, name="signup"),
    path('login/', views2.handleLogin, name="login"),
    path('logout/', views2.handleLogout, name="logout"),
    path('displayall/', views.DisplayAll, name="display"),
    path('deletePost/<str:slug>', views.deletePost, name="delete"),
    # Remove This
    path('test/<str:slug>', views.test, name='Test'),
]