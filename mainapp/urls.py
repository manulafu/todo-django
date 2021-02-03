from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
	path('', views.index, name='index'),
	path('create/', views.CreateTask.as_view(), name='create-task'),
	path('<int:pk>/delete/', views.DeleteTask.as_view(), name='delete-task'),
	path('<int:pk>/update/', views.UpdateTask.as_view(), name='update-task')
]