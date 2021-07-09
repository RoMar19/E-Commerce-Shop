from django.db import models
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    size_38 = '38'
    size_39 = '39'
    size_40 = '40'
    size_41 = '41'
    size_42 = '42'
    size_43 = '43'
    size_44 = '44'
    CHOOSE_SIZE = (
        ('choose_size', ('Choose your size')),
        ('38', ('size_38')),
        ('39', ('size_39')),
        ('40', ('size_40')),
        ('41', ('size_41')),
        ('42', ('size_42')),
        ('43', ('size_43')),
        ('44', ('size_44')),
    )
    size = models.CharField(max_length=120, choices=CHOOSE_SIZE, default='choose_size')
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.product_name
