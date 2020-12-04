from django.contrib import admin
import Vehicle_Specification.models as models
import nested_admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PartBrandAdmin(ImportExportModelAdmin):
    list_display = ('name', )


class PartImageInline(admin.TabularInline):
    model = models.PartImage
    extra = 1

class CategoryL1Admin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    prepopulated_fields = {"slug": ("name",)}


class CategoryL2Admin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'image')
    prepopulated_fields = {"slug": ("name",)}


class CategoryL3Admin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'image')
    prepopulated_fields = {"slug": ("name",)}

class PartAdmin(ImportExportModelAdmin):
    list_display = ('name', 'part_number', 'brand', 'description', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('fitment',)
    inlines = [PartImageInline]


class VehicleInline(nested_admin.NestedTabularInline):
    model = models.Vehicle
    extra = 0


class VehicleModelInline(nested_admin.NestedStackedInline):
    model = models.VehicleModel
    extra = 0
    inlines = [VehicleInline]


class VehicleMakeAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', )
    inlines = [VehicleModelInline]


class VehicleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'make', 'model', 'year_start', 'year_end', 'engine', 'trim')
    def make(self, obj):
        return obj.model.make


class VehicleModelAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', )
    inlines = [VehicleInline]

admin.site.register(models.CategoryL1, CategoryL1Admin)
admin.site.register(models.CategoryL2, CategoryL2Admin)
admin.site.register(models.CategoryL3, CategoryL3Admin)
admin.site.register(models.VehicleMake, VehicleMakeAdmin)
admin.site.register(models.VehicleModel, VehicleModelAdmin)
admin.site.register(models.Vehicle, VehicleAdmin)
admin.site.register(models.PartBrand, PartBrandAdmin)
admin.site.register(models.Part, PartAdmin)

