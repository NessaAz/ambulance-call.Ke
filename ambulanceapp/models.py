from django.db import models
from django.contrib.auth.models import User


class Ambulanceprovider(models.Model):
    user_rec = models.ForeignKey(User, on_delete=models.CASCADE)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=50)
    town = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'Ambulanceproviders'

    def __unicode__(self):
        return u"%s's Provider Info" % self.user_rec
