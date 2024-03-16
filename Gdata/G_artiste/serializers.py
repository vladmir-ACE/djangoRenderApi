from rest_framework import serializers

from G_artiste.models import Artiste


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artiste
        fields = '__all__'
        