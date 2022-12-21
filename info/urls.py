from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
]