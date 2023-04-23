"""CoderApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from CoderApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name = "Inicio"), #Primera view
    path("cursos", views.cursos, name = "cursos"),
    path("profesores", views.profesores, name = "profesores"),
    path("estudiantes", views.estudiantes, name= "estudiantes"),
    path("entregables", views.mostrar_entregables, name = "entregables"),
    path("buscarcurso", views.buscar_curso, name = "buscarcurso"),
    path('estudiantes/list', views.EstudiantesList.as_view(), name='List'),
    path('estudiantes/<int:pk>', views.EstudiantesDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.EstudiantesCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.EstudiantesUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EstudiantesDelete.as_view(), name='Delete'),
    path("leerprofesores", views.leerprofesores, name= "LeerProfesores"),
    path("eliminarprofesor/<profesor_nombre>/", views.eliminarprofesor, name = "EliminarProfesor"),
    path("editarprofesores/<profesor_nombre>/", views.editarprofesor, name = "EditarProfesor"),
    path("login", views.login_request, name="Login"),
    path("register", views.register, name= "Register"),
    path("logout", LogoutView.as_view(template_name = "CoderApp/inicio.html"), name="Logout"),
    path("editarusuario", views.editarperfil, name = "editarperfil"),
    path("agregaravatar", views.agregarAvatar, name="agregaravatar"),
    path('cursos/list', views.CursosList.as_view(), name='CursoList'),
    path('cursos/<int:pk>', views.CursosDetalle.as_view(), name='CursoDetail'),
    path('cursos/nuevo', views.CursosCreacion.as_view(), name='CursoNew'),
    path('cursos/editar/<int:pk>', views.CursosUpdate.as_view(), name='CursoEdit'),
    path('cursos/eliminar/<int:pk>', views.CursosDelete.as_view(), name='CursoDelete'),
    path("perfil/<int:pk>", views.UsuarioDetalle.as_view(), name="perfil"),

    path("post/list", views.PostList.as_view(), name="post-list"),
    path("post/upload", views.postear, name="post-upload"),
    path("post/detail", views.PostDetail.as_view(), name="post-detail"),
    path("post/delete", views.PostDelete.as_view(), name="post-delete"),

    #path("busquedadecurso", views.curso_busqueda)
]