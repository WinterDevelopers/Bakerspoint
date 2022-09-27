from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from company.models import Categories

# Create your models here.

#product weight chioces
WEIGHT = (
    ("500g","500g"),
    ("1kg","1kg"),
    ("2.5kg", "2.5kg"),
    ("5kg", "5kg")
)
class ProductCategories(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True,blank=True)
    image = models.ImageField(upload_to='media/store/products')

    def save(self, *args, **kwargs):
   
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('products', kwargs = {'slug':self.slug})

class Product(models.Model):
    product_category = models.ForeignKey(ProductCategories, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500)
    weight = models.CharField(max_length=10,choices=WEIGHT, default='500g')

    def __str__(self) -> str:
        return str(self.product_category)+" of "+self.weight

    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/store/products')
    alt = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return 'Image for '+ str(self.product)

class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    user = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.CharField(max_length=100)
    show = models.BooleanField(default=False)

    def __str__(self) -> str:
        return 'review for '+self.Product


class Order(models.Model):
    customer = models.CharField(max_length=100)
    date_orderd = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    data_added = models.DateField(auto_now_add=True)
