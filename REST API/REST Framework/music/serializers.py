from rest_framework import serializers
from .models import Music, Artist


# ArtistListSerializer
    # 모든 가수의 정보를 반환하기 위한 Serializer
    # id, name 필드 출력
class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name')
        read_only_fields = ('artist',)


# MusicListSerializer
    # 모든 음악의 정보를 반환하기 위한 Serializer
    # id, title 필드 출력
class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title',)


# MusicSerializer
    # 상세 음악의 정보를 생성 및 반환하기 위한 Serializer
    # id, title, artist 필드 출력
class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist',)

# ArtistSerializer
    # 상세 가수의 정보를 생성 및 반환하기 위한 Serializer
    # id, name, music_set, music_count 필드 출력
    # (music_count 필드는 music_set을 count한 결과이다.)
class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'