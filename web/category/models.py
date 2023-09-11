from django.db import models
from django.contrib import sessions


class Category(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Author(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="Author ni ismi")
    bio = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Mualif"
        verbose_name_plural = ("Mualiflar"
                               "")


class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kitobni nomi")
    image = models.ImageField(upload_to="book/")
    titile = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    price1 = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} || {self.author}"

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
        ordering = ['-id']


class Blogimage(models.Model):
    image = models.ImageField(max_length=30)

    def __str__(self):
        return self.image

class Blog(models.Model):
    name = models.CharField(max_length=50)
    title = models.TextField()
    img = models.ManyToManyField(Blogimage, verbose_name="image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


class DiscountImage(models.Model):
    image = models.ImageField(upload_to="cher/")


    def __str__(self):
        return self.image


class Discount(models.Model):
    discount = models.CharField(max_length=50, verbose_name="Chegirma narxi")
    image = models.ManyToManyField(DiscountImage, verbose_name="image")
    price = models.IntegerField()
    title = models.TextField()


    def __str__(self):
        return self.discount