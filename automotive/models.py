from django.db import models

from autoslug import AutoSlugField


class Brand(models.Model):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name


class ModelManager(models.Manager):
    def get_query_set(self):
        return super(ModelManager, self).get_queryset().prefetch_related('brand')


class Model(models.Model):
    brand = models.ForeignKey(Brand)
    name = models.CharField(max_length=64)
    full_name = models.CharField(max_length=256, blank=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)

    objects = ModelManager()

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = u'{} {}'.format(self.brand, self.name)
        return super(Model, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.full_name or self.name
