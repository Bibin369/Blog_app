from rest_framework import serializers
from login.models import registeration

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model=registeration
        fields=(
            'name',
            'image',
            'email',
            'password'
        )