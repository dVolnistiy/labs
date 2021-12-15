from django.contrib import admin

from .models import Building, Floor, Proc, Room, PC, Workplace

admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(PC)
admin.site.register(Workplace)
#admin.site.register(Proc)

# Register your models here.
