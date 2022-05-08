from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('create-task/', views.TaskCreate.as_view(), name='create-item'),
    path('update-task/<int:pk>/', views.TaskUpdate.as_view(), name='update-item'),
    path('delete-task/<int:pk>/', views.TaskDelete.as_view(), name='delete-item'),
]
