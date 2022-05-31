from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    content = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = "article"

class Category(models.Model):
    category_name = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)

    class Meta:
        db_table = "category"