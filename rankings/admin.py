from django.contrib import admin
from .models import Indicator, IndicatorIndex, GroupName

# Custom admin class for Indicator
@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('state', 'group', 'indicator', 'value', 'year')  # Replace with actual fields
    search_fields = ('state', 'group', 'indicator', 'value', 'year')  # Fields to be searchable

# Custom admin class for IndicatorIndex
@admin.register(IndicatorIndex)
class IndicatorIndexAdmin(admin.ModelAdmin):
    list_display = ('group', 'indicator')
    search_fields = ('group', 'indicator')   
    ordering = ('group',)   

# Custom admin class for IndicatorIndex
@admin.register(GroupName)
class GroupNameAdmin(admin.ModelAdmin):
    list_display = ('index', 'name')
    search_fields = ('index', 'name')  # Fields to be searchable
