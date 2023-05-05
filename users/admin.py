from django.contrib import admin

from users import models


class RelationshipInline(admin.StackedInline):
    model = models.Relationship
    fk_name = 'from_person'


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.Pending)
