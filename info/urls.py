from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/delete/<int:id>/',views.delete,name='delete'),
    path('dashboard/update/<int:id>/',views.update,name='update'),
]