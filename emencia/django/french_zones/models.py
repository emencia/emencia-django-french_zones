"""Models for emencia.django.french_zones"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Region(models.Model):
    code = models.CharField(_('code INSEE'), max_length=2, primary_key=True)
    name = models.CharField(_('official name'), max_length=128)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('region')
        verbose_name_plural = _('regions')
        ordering = ('name',)

class Department(models.Model):
    region = models.ForeignKey(Region, verbose_name=_('region'))
    
    code = models.CharField(_('code'), max_length=3, primary_key=True)
    name = models.CharField(_('official name'), max_length=128)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')
        ordering = ('code',)



