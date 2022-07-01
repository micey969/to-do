from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('delete/<int:id>', views.Delete, name='Delete'),
    path('incomplete/<int:id>', views.InComplete, name='InComplete'),
    path('complete/<int:id>', views.Complete, name='Complete'),
]
