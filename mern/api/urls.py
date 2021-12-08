from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    # path('model-list/', views.modelsList, name="api-overview")

    path('login',views.login),
    # Users
    path('users/all',views.usersList),

    # Users
    path('users/',views.usersList, name='Userslist'),
    path('users/get/<id>',views.usersGet, name='UsersGet'),
    path('users/create/',views.usersCreate, name='Userstore'),
    path('users/update/<id>',views.usersUpdate, name='UsersUpdate'),
    path('users/delete/<id>',views.usersDelete, name='UsersDelete'),

    # Projects
    path('projects/user/<id>',views.projectsUsuario, name='Projectslist'),
    path('projects/get/<id>',views.projectsGet, name='ProjectGet'),
    path('projects/create/',views.projectsCreate, name='ProjectStore'),
    path('projects/update/<id>',views.projectsUpdate, name='ProjectUpdate'),
    path('projects/delete/<id>',views.projectsDelete, name='ProjectDelete'),

    # Tasks
    path('tasks/project/<id>',views.tasksProject, name='Taskslist'),
    path('tasks/get/<id>',views.tasksGet, name='tasksGet'),
    path('tasks/create/',views.tasksCreate, name='tasksCreate'),
    path('tasks/update/<id>',views.tasksUpdate, name='tasksUpdate'),
    path('tasks/delete/<id>',views.tasksDelete, name='tasksDelete'),
]