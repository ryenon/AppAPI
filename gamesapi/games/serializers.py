#from typing_extensions import Required
from rest_framework import serializers
from games.models import Game

class GameSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()
    game_category = serializers.CharField(max_length=200)
    played = serializers.BooleanField(required=True)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(sef, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.game_category = validated_data.get('game_category', instance.game_category)
        instance.played = validated_data.get('palyed', instance.played)
        instance.save()
        return instance

    try:
        from typing_extensions import Required
    except ImportError:
        from typing import Generic, TypeVar

        T = TypeVar("T")

        class Required(Generic[T]):
            pass