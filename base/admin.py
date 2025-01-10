from django.contrib import admin
from .models import Entidad, Proyecto, Usuenti, Seguimiento, UsuDomain
from django.contrib.auth.models import Group, User

admin.site.register(Entidad)
admin.site.register(Proyecto)
admin.site.register(Usuenti)
admin.site.register(Seguimiento)
admin.site.register(UsuDomain)

# Desregistrar los modelos Group y User
admin.site.unregister(Group)
admin.site.unregister(User)