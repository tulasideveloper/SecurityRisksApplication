from django.contrib import admin
from django.urls import path
from .views import Load_HomePage, Load_AddRiskAspect, Load_EditRiskAspect,Load_ViewRiskAspect
urlpatterns = [    
    path('Load_AddRiskAspect', Load_AddRiskAspect, name='Load_AddRiskAspect'),
    path('Load_ViewRiskAspect/<int:id>', Load_ViewRiskAspect, name='Load_ViewRiskAspect'),
    path('Load_EditRiskAspect/<int:id>', Load_EditRiskAspect, name='Load_EditRiskAspect'),
    path('',Load_HomePage, name='Load_HomePage')
]