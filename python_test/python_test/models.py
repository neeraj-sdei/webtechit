# Insert models here
from django.db import models
from django.forms import ModelForm


class Client(models.Model):
    client_name = models.CharField(max_length=100, null=False,
                                   blank=False, unique=True)
    street_name = models.CharField(max_length=50, null=True, blank=True)
    suburb = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=12, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.IntegerField(max_length=15, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return '{}'.format(self.client_name)


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
