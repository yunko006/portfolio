from rest_framework import serializers
from .models import ProjetPro


class ProjetProtSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "nom",
            "description",
            "categorie",
            "start_date",
            "end_date",
            "url",
            "github",
            "logo",
            "technologies",
            "clients",
            "lien_clients",
            "problemes_resolus",
        )

        model = ProjetPro
