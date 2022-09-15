from django.contrib import admin

from .models import Categoria, Projeto


class CategoriaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CategoriaAdmin)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    ...
