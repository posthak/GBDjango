import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mob_number = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    date_reg = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, mob_number: {self.mob_number}' \
               f', address: {self.address}, date_reg: {self.date_reg}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to='product/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_created = models.DateField(default=datetime.datetime.today)

    def __str__(self):
            return f'name: {self.name}, description: {self.description}, price: {self.price}' \
                   f', quantity: {self.quantity}, date_created: {self.date_created}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return f'total_price: {self.total_price}, order_date: {self.order_date}'

