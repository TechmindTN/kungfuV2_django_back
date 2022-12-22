from django.contrib import admin
from .models import Licences,Profile,Athlete,Coach,Arbitrator,Club,Supporter,Seasons,Grade,Degree,Categorie,Discipline,role,Ligue,ArchivedLicences,Weights



@admin.register(Weights)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Weights._meta.get_fields()]
@admin.register(ArchivedLicences)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedLicences._meta.get_fields()]
@admin.register(Ligue)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ligue._meta.get_fields()]
@admin.register(role)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in role._meta.get_fields()]
@admin.register(Coach)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Coach._meta.get_fields()]
@admin.register(Arbitrator)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Arbitrator._meta.get_fields()]
@admin.register(Club)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Club._meta.get_fields()]
@admin.register(Supporter)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Supporter._meta.get_fields()]
@admin.register(Seasons)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Seasons._meta.get_fields()]
@admin.register(Grade)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Grade._meta.get_fields()]
# @admin.register(Degree)
# class RequestDemoAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Discipline._meta.get_fields()]
# @admin.register(Discipline)
# class RequestDemoAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Athlete._meta.get_fields()]
@admin.register(Categorie)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Categorie._meta.get_fields()]

@admin.register(Athlete)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Athlete._meta.get_fields()]

@admin.register(Profile)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]

@admin.register(Licences)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Licences._meta.get_fields()]