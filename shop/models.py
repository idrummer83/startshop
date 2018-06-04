from django.db import models
from django.urls import reverse
from filer.fields.image import FilerImageField
from ckeditor.fields import RichTextField

# Create your models here.

class productCategory(models.Model):
    name = models.CharField('наименование категории', max_length=250)
    slug = models.SlugField(verbose_name='Slug', max_length=150, unique=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=True)
    image = FilerImageField(on_delete=models.CASCADE, related_name='product_cat_image', verbose_name='изображение категории', null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = RichTextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'категория продукта'
        verbose_name = 'категория продукта'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(productCategory, on_delete=models.CASCADE, related_name='prod_of_category', verbose_name='категория', blank=True)
    name = models.CharField('наименование продукта', max_length=250)
    slug = models.SlugField(verbose_name='Slug', max_length=150, unique=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = FilerImageField(on_delete=models.CASCADE, related_name='product_image',
                              verbose_name='изображение продукта', null=True, blank=True,)
    description = RichTextField(verbose_name='Описание', null=True, blank=True)
    long_description = RichTextField(verbose_name='Описание большое', null=True, blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
