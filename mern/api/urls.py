from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    # path('model-list/', views.modelsList, name="api-overview")

    path('login',views.login),
    # Users
    path('users/all',views.usersList),

    # Projects
    path('projects/user/<id>',views.projectsUsuario, name='Projectslist'),
    path('projects/get/<id>',views.projectsGet, name='ProjectGet'),
    path('projects/create/',views.projectsCreate, name='ProjectStore'),
    path('projects/update/<id>',views.projectsUpdate, name='ProjectUpdate'),
    path('projects/delete/<id>',views.projectsDelete, name='ProjectDelete'),
]