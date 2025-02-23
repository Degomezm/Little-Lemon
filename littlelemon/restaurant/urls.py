from django.urls import path
from . import views
from .views import MenuItemView, SingleMenuItemView

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]
