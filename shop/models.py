from django.db import models

# Create your models here.
from django.urls import reverse


class categ(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)

    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

class products(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    img=models.ImageField(upload_to='products')
    desc=models.TextField(max_length=300)
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])

class cartlist(models.Model):
    cart_id=models.CharField(max_length=100,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class items(models.Model):
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.prodt