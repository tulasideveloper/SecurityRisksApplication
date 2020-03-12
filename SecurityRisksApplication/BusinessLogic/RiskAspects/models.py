from django.db import models

# Create your models here.

class SecurityRiskAspects(models.Model):
    id = models.AutoField(primary_key=True)
    RiskAspect_Name = models.CharField('Risk Aspect Name',null=False, blank=False,max_length=200)
    RiskAspect_Description = models.TextField('Risk Aspect Description',null=False, blank=False)
    CreatedDate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.RiskAspect_Name

    # order Risk Aspects
    class Meta:
        ordering = ['id']
    
