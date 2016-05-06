from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    class Meta:
        ordering = ["full_name"]
    def __str__(self):
        return "{full_name}".format(full_name=self.full_name)
    def __unicode__(self):
        return self.__str__()

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return "{name}".format(name=self.name)
    def __unicode__(self):
        return self.__str__()

class ReadingLevel(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return "{name}".format(name=self.name)
    def __unicode__(self):
        return self.__str__()

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author, models.SET_NULL,
                               null=True, blank=True, default=None)
    category = models.ManyToManyField(Category, default=None)
    reading_level = models.ForeignKey(ReadingLevel, models.SET_NULL,
                                      null=True, blank=True, default=None)
    description = models.TextField()
    class Meta:
        ordering = ["title"]
    def __str__(self):
        return "{title}".format(title=self.title)
    def __unicode__(self):
        return self.__str__()
