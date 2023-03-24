
from django.urls import path
from .import views

urlpatterns = [
	path('', views.home, name='home'),
	path('media/', views.media_list, name='media_list'),
	path('view_video/<int:pk>/', views.view_video, name='view_video'),
	path('contact/', views.contact, name='contact'),
	path('search/', views.search, name='search'),
	path('about/', views.about, name='about'),
    path('create_media/upload/', views.create, name='create'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('image/<int:pk>/thumbnail/', views.model_thumbnail, name='model_thumbnail'),

]