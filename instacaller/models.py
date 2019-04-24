from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.db import models
import jsonfield
# Create your models here.

class UserDB(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    is_spam = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)

    def __unicode__(self):
    	return self.name + "-->"

class UserContactDB(models.Model):
	registered_user = models.ForeignKey(UserDB,related_name='r_user')
	contacts = models.ManyToManyField(UserDB,related_name='contacts_list')

	def __unicode__(self):
		return "contacts of ---> " + self.user_id.name	