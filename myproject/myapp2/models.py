from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mob_number = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, mob_number: {self.mob_number}' \
               f', address: {self.address}, date_reg: {self.date_reg}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f'name: {self.name}, description: {self.description}, price: {self.price}' \
                   f', quantity: {self.quantity}, date_created: {self.date_created}'

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'total_price: {self.total_price}, date_ordered: {self.date_ordered}'

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     def __str__(self):
#         return f'Name: {self.name}, email: {self.email}'
#
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     def __str__(self):
#         return f'Title is {self.title}'
#
#     def get_summary(self):
#        words = self.content.split()
#        return f'{" ".join(words[:12])}...'
