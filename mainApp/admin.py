from django.contrib import admin

from news.models import Articles
from master_office.models import Master,Order, OrderLine, Comment
from mainApp.models import Area, Service

admin.autodiscover()


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'time', 'price', 'area')
    list_filter = ('price', 'time', 'area')
    pass


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_areas',  'phone', 'rating')
    list_filter = ('rating',)
    pass
# 'get_user', 'get_areas', 'get_client', 'get_master',

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_client', 'status', 'rating', 'price')
    list_filter = ('rating', 'status', 'price')
    pass


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = ( 'order_id', 'status', 'brand_name')
    list_filter = ('status', 'brand_name')
    pass




admin.site.register(Articles)

admin.site.register(Comment)
#admin.site.register(Area, AreaAdmin)
#admin.site.register(Service, ServiceAdmin)

