from django.db import models


class Author(models.Model):
    fio = models.CharField(max_length=255)

    def __str__(self):
        return self.fio


class Presentation(models.Model):
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    creation_date = models.DateField(null=True, blank=True)
    descript = models.TextField(null=True, blank=True)
    image_name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='presentations')

    def __str__(self):
        return self.title

