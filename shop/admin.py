from django.contrib import admin
from . models import *
# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,catadmin)

class proadmin(admin.ModelAdmin):
    list_display = ['name','price','available','stock','available','img']
    list_editable = ['price','stock','available','img']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,proadmin)

admin.site.register(cartlist)
admin.site.register(items)