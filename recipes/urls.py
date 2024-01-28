from django.urls import path
# from recipes.views import home
# from recipes import views
from . import views
# from recipes.views import home, about, contact

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
