from django.contrib import admin

from .models import Building, Floor, Room, PC, Workplace

admin.site.register(Building)

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('floor', 'building')
# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'floor', 'building')

@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    list_display = ('place', 'room')

@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    list_display = ('pc', "place")