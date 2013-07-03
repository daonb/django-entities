from django.contrib import admin
from entities.models import Domain, Division, Entity

class DomainAdmin(admin.ModelAdmin):
    pass

class DivisionAdmin(admin.ModelAdmin):
    pass

class EntityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Domain, DomainAdmin)
admin.site.register(Entity, EntityAdmin)
admin.site.register(Division, DivisionAdmin)
