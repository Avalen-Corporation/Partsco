from django.db import models
import datetime
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey

# Create your models here.


YEAR_CHOICES = [(r, r) for r in range(1990, datetime.date.today().year + 1)]

TRIM = (
    ('XLE', 'Exclusive Limited Edition'),
    ('LE', 'Limited Edition'),
    ('SE', 'Standard Edition'),
)


class CategoryL1(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=35, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='category_images/')

    class Meta:
        verbose_name_plural = "Category Level 1"

    def __str__(self):
        return self.name


class CategoryL2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=35, unique=True)
    category = models.ForeignKey(CategoryL1, on_delete=models.SET_NULL, null=True, related_name='categories')
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='category_images/')

    class Meta:
        unique_together = ('name', 'category')
        verbose_name_plural = "Category Level 2"

    def __str__(self):
        return self.name


class CategoryL3(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=35, unique=True)
    category = models.ForeignKey(CategoryL2, on_delete=models.SET_NULL, null=True, related_name='categories')
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='category_images/')

    class Meta:
        unique_together = ('name', 'category')
        verbose_name_plural = "Category Level 3"

    def __str__(self):
        return self.name


class PartBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "4. Part Brands"


class VehicleMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "1. Vehicle Makes"

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.ForeignKey(VehicleMake, on_delete=models.SET_NULL, null=True, related_name='vehicle_models')
    name = models.CharField(max_length=50, )

    # year = models.IntegerField(choices=YEAR_CHOICES)

    class Meta:
        unique_together = ('make', 'name')
        verbose_name_plural = "2. Vehicle Models"

    def __str__(self):
        return u'%s' % self.name


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.ForeignKey(VehicleMake, on_delete=models.SET_NULL, null=True, related_name='vehicles')
    model = ChainedForeignKey(VehicleModel, chained_field='make', chained_model_field='make',
                              on_delete=models.SET_NULL, show_all=False, auto_choose=True, sort=True,
                              default=None, null=True, related_name='vehicles')
    year_start = models.IntegerField(choices=YEAR_CHOICES)
    year_end = models.IntegerField(choices=YEAR_CHOICES)
    engine = models.CharField(max_length=50)
    trim = models.CharField(choices=TRIM, max_length=50)

    class Meta:
        unique_together = ('model', 'year_start', 'year_end', 'engine', 'trim')
        verbose_name_plural = "3. Vehicles"

    def __str__(self):
        return u'%s %s %s %s %s ' % (self.model, str(self.year_start), str(self.year_end), self.engine, self.trim)


class Part(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(PartBrand, related_name='parts', on_delete=models.SET_NULL, blank=True, null=True)
    category_l1 = models.ForeignKey(CategoryL1, related_name='parts', on_delete=models.PROTECT)
    category_l2 = ChainedForeignKey(CategoryL2, related_name='parts', on_delete=models.SET_NULL, blank=True, null=True,
                                    chained_field="category_l1", chained_model_field="category")
    category_l3 = ChainedForeignKey(CategoryL3, related_name='parts', on_delete=models.SET_NULL, blank=True, null=True,
                                    chained_field="category_l2", chained_model_field="category")
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=260, unique=True,
                            help_text='Unique value for shop page URL, created from name.')
    part_number = models.CharField(max_length=30)
    # sku = models.IntegerField(unique=True)
    # Todo: Cascading dropdown in parts, no djpipchanging of super category in categories | NOT A SOLID FIX
    # price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    fitment = models.ManyToManyField(Vehicle, blank=True)
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "5. Part"
        unique_together = ('name', 'part_number')

    def __str__(self):
        return u'%s %s' % (self.name, self.part_number)


class PartImage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='part_images/')
    part = models.ForeignKey(Part, on_delete=models.SET_NULL, null=True, related_name='images')
