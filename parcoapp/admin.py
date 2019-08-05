from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import *

@admin.register(Entry)
class EntryAdmin(OSMGeoAdmin):
    default_lon = 1077844
    default_lat = 5486400
    default_zoom = 12

class AllegatiInline(admin.StackedInline):
    model = Allegato
    extra = 1

class DettaglioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['descrizione_dettaglio', 'data_dettaglio', 'fase_dettaglio', 'lavoro_dettaglio']})
    ]
    inlines = [AllegatiInline, ]

admin.site.register(Categoria)
admin.site.register(Fase)
admin.site.register(Lavoro)
admin.site.register(Dettaglio, DettaglioAdmin)
