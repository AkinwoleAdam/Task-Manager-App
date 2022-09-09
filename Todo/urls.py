from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   
   path('register/',views.register,name='register'),
   
   path('login/',views.loginUser,name='login'),
   
   path('profile/',views.profile,name='profile'),
   
   path('logout/',views.logoutUser,name='logout'),
   
   path('new_todo',views.newTodo,name='new_todo'),
   
   path('update/<str:pk>',views.updateTodo,name='update'),
   
   path('delete/<str:pk>',views.deleteTodo,name='delete'),
   
   path('report',views.report,name='report'),
   
]