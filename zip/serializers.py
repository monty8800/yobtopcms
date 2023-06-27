from rest_framework import serializers

from zip.models import ZipCode


class ZipCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZipCode
        fields = ['code', 'country', 'city']
