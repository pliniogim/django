from django.urls import path
# from recipes.views import home
# from recipes import views
from . import views
# from recipes.views import home, about, contact

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]
