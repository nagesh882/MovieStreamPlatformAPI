from rest_framework import serializers
from .models import StreamPlatform, WatchList, Review


class WatchListSerializer(serializers.ModelSerializer):
    platform = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'

        def get_photo_url(self, obj):
            request = self.context.get('request')
            photo_url = obj.fingerprint.url
            return request.build_absolute_url(photo_url)


class StreamPlatformSerializer(serializers.ModelSerializer):
    movie_list = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'

        def get_photo_url(self, obj):
            request = self.context.get('request')
            photo_url = obj.fingerprint.url
            return request.build_absolute_url(photo_url)



class ReviewSerializer(serializers.ModelSerializer):
    WatchList = WatchListSerializer(many=False, read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

        def get_photo_url(self, obj):
            request = self.context.get('request')
            photo_url = obj.fingerprint.url
            return request.build_absolute_url(photo_url)