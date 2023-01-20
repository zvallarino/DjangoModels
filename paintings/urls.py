from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_painting/',views.PaintingCreateView.as_view(),name='create_painting'),
    path('painting/<int:pk>',views.PaintingDetailView.as_view(),name='painting_detail'),
    path('sonic/',views.sonic,name='sonic'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('profile',views.CheckedOutBooksByUserView.as_view(),name='profile')
]