from django.contrib import admin

from customer.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Customer, CustomerAdmin)