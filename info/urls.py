from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_animals, name='all_animals'),
    path('single/<int:id>', views.single_animal, name='single_animal')
]