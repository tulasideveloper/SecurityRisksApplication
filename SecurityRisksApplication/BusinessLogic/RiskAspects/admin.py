from django.contrib import admin
from .models import SecurityRiskAspects
# Register your models here.

class SecurityRiskAspectsAdmin(admin.ModelAdmin):
    list_display = ['RiskAspect_Name', 'RiskAspect_Description','CreatedDate']
    class Meta:
        model = SecurityRiskAspects

admin.site.register(SecurityRiskAspects, SecurityRiskAspectsAdmin)
