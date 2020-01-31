from django.urls import path

from . import views

urlpatterns = [
    path('logistic', views.logistic_regression),
    path('xgboost', views.xgboost),
    path('random_forest', views.random),
]