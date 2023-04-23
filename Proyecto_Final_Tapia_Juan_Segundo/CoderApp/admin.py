from django.contrib import admin

# Register your models here.

from CoderApp.models import *
admin.site.register(Catedra)
admin.site.register(Entregado)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Avatar)
admin.site.register(Post)
