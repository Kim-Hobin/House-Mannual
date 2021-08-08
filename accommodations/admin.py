from django.contrib import admin
from . import models


class TouristAttractionInline(admin.TabularInline):

    model = models.TouristAttraction


@admin.register(models.Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    inlines = (TouristAttractionInline,)
