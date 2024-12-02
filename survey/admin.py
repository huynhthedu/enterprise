from django.contrib import admin
from .models import StrategyOperation

from .models import GeneralInformation, Business, BusinessType, BusinessField, BusinessSize, StrategyOperation, GeneralFeedback

admin.site.register(GeneralInformation)
admin.site.register(BusinessType)
admin.site.register(BusinessField)
admin.site.register(BusinessSize)
admin.site.register(StrategyOperation)
admin.site.register(GeneralFeedback)

admin.site.unregister(StrategyOperation)

@admin.register(StrategyOperation)
class StrategyOperationAdmin(admin.ModelAdmin):
    list_display = ['id', 'submitted_at']