from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    # path('model-list/', views.modelsList, name="api-overview")

    path('login',views.login),
    # Users
    path('users/all',views.usersList)
]