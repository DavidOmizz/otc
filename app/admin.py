from django.contrib import admin
from .models import CohortInfo

# Register your models here.
# admin.site.register(CohortInfo)

@admin.register(CohortInfo)
class CohortInfoAdmin(admin.ModelAdmin):
    list_display = ('name','location', 'niche','student')
