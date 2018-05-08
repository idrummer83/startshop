from django.db import models
from filer.fields.image import FilerImageField
from ckeditor.fields import RichTextField

# Create your models here.

class baseImage(models.Model):
     image = FilerImageField(verbose_name='Изображение', on_delete=models.CASCADE, null=True, blank=True,
                          related_name='photo')


class productCategory(models.Model):
    name = models.CharField('наименование категории', max_length=250)
    slug = models.SlugField(verbose_name='Slug', max_length=64, unique=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=True)
    image = models.ForeignKey(baseImage, on_delete=models.CASCADE, related_name='product_image', verbose_name='изображение категории')
    # image = FilerImageField(verbose_name='Изображение категории', related_name='product_image', null=True, blank=True)
    description = RichTextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'категория продукта'
        verbose_name = 'категория продукта'

    def __str__(self):
        return self.name



class Product(productCategory):
    long_description = RichTextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
