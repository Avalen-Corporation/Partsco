from django.db import models
from smart_selects.db_fields import ChainedForeignKey
# from Vehicle_Specification.models import CategoryL1, CategoryL2, CategoryL3


# Create your models here.

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
    category = models.ForeignKey(CategoryL1, on_delete=models.CASCADE, related_name='categories')
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
    category = models.ForeignKey(CategoryL2, on_delete=models.CASCADE, related_name='categories')
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='category_images/')

    class Meta:
        unique_together = ('name', 'category')
        verbose_name_plural = "Category Level 3"

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=3)
    category_l1 = models.ForeignKey(CategoryL1, related_name='product', on_delete=models.PROTECT)
    category_l2 = ChainedForeignKey(CategoryL2, related_name='product', on_delete=models.SET_NULL, blank=True, null=True,
                                    chained_field="category_l1", chained_model_field="category")
    category_l3 = ChainedForeignKey(CategoryL3, related_name='product', on_delete=models.SET_NULL, blank=True, null=True,
                                    chained_field="category_l2", chained_model_field="category")
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)