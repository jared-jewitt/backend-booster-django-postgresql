from rest_framework import serializers

from src.v1.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance

    class Meta:
        model = Post
        fields = "__all__"
