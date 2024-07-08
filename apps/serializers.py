from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name', 'text', 'image', 'created_at', 'updated_at']

    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('le champ  dois pas etre  moins 5 caratères')
        return value
    
    def validate_text(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Le contenu doit contenir au moins 10 caractères')
        return value