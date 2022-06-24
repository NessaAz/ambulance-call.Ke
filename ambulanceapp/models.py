from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
from django.urls import reverse
from cloudinary.models import CloudinaryField



class Ambulanceprovider(models.Model):
    user_rec = models.ForeignKey(User, on_delete=models.CASCADE)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=50)
    town = models.CharField(max_length=20)
    stripe_id = models.CharField(max_length=16, blank=True)
    image = CloudinaryField('images', default='image')


    class Meta:
        verbose_name_plural = 'Ambulanceproviders'

    def __unicode__(self):
        return u"%s's Provider Info" % self.user_rec


class Account(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=50)
    town = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    image = CloudinaryField('images', default='image')


    class Meta:
        verbose_name_plural = 'accounts'

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse( 'account_detail', [self.uuid])

    def get_update_url(self):
        return reverse('account_update', [self.uuid])

    def get_delete_url(self):
        return reverse ('account_delete', [self.uuid])
    
    
class Contact(models.Model):
    uuid = ShortUUIDField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contacts'

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __unicode__(self):
        return u'%s' % self.full_name

    def get_absolute_url(self):
        return reverse('contact_detail', [self.uuid])

    def get_update_url(self):
        return reverse('contact_update', [self.uuid])

    def get_delete_url(self):
        return reverse('contact_delete', [self.id])
    
       