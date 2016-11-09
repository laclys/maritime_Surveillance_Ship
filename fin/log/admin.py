from django.contrib import admin
from log.models import User2,Ship
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'number','position','email','firstname','lastname','phone','address')
    search_fields = ('username','number',)
    
class ShipAdmin(admin.ModelAdmin):

    list_display = ('dtmGPS','floLON', 'vchLonUnit', 'floLAT','vchLatUnit','floSPD','floDIR','floHDT','floHDM','floWST','floWSR','floWDT','floWDR','vchWdtUnit','floDPT','floVLW')
    list_display = ('dtmGPS',)
    list_filter = ('dtmGPS',)
    date_hierarchy = 'dtmGPS'
    ordering = ('-dtmGPS',)


admin.site.register(User2, UserAdmin)
admin.site.register(Ship, ShipAdmin)
