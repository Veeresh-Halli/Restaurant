from django.db import models

# Create your models here.
class Category(models.Model):
  title = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
        return self.title

class Foodtype(models.Model):
  title = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
        return self.title

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    food_type = models.ForeignKey(Foodtype, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

