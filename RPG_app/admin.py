from django.contrib import admin # type: ignore

from .models import Categoria, Cuenta, CuentaPersonaje, Item, Personaje


class CuentaPersonajeInline(admin.TabularInline):
    model = CuentaPersonaje
    extra = 0


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "correo")
    search_fields = ("usuario", "correo")
    inlines = [CuentaPersonajeInline]


@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ("id", "raza", "descripcion", "nivel", "ban", "creado")
    list_filter = ("ban", "raza")
    inlines = [ItemInline]


@admin.register(CuentaPersonaje)
class CuentaPersonajeAdmin(admin.ModelAdmin):
    list_display = ("id", "cuenta", "personaje")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "tipo")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "categoria", "personaje", "nivel", "cantidad")
    list_filter = ("categoria",)
    search_fields = ("nombre",)

