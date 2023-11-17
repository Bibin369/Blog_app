from rest_framework import serializers
from post.models import postmodel

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model=postmodel
        fields=(
            'userid',
            'title',
            'message',
        )