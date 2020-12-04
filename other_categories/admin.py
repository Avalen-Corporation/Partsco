from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
import other_categories.models as models

# Register your models here.

class Other_Product(admin.ModelAdmin):
    list_display = ('name', 'description',  'is_available')
    prepopulated_fields = {'slug': ('name',)}
    # inlines = [PartImageInline]


class CategoryL1Admin(admin.ModelAdmin):
        list_display = ('name', 'description', 'image')
        prepopulated_fields = {"slug": ("name",)}

class CategoryL2Admin(admin.ModelAdmin):
        list_display = ('name', 'category', 'description', 'image')
        prepopulated_fields = {"slug": ("name",)}

class CategoryL3Admin(admin.ModelAdmin):
        list_display = ('name', 'category', 'description', 'image')
        prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.CategoryL1, CategoryL1Admin)
admin.site.register(models.CategoryL2, CategoryL2Admin)
admin.site.register(models.CategoryL3, CategoryL3Admin)
admin.site.register(models.Product, Other_Product)
