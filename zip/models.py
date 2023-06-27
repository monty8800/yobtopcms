from django.db import models


class ZipCode(models.Model):
    COUNTRIES = (
        ('US', 'com'),
        ('CN', 'cn'),
        ('JP', 'co.jp'),
        ('CA', 'ca'),
        ('MX', 'com.mx'),
        ('UK', 'co.uk'),
        ('DE', 'de'),
        ('FR', 'fr'),
        ('IT', 'it'),
        ('ES', 'es'),
        ('NL', 'nl'),
        ('PL', 'pl'),
        ('SE', 'se'),
        ('AU', 'au'),
        ('IN', 'in'),
        ('SA', 'sa'),
        ('AE', 'ae'),
        ('TR', 'tr'),
        ('SG', 'sg'),
        ('BR', 'br'),
    )
    code = models.CharField(max_length=10, primary_key=True)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    city = models.CharField(max_length=20)
