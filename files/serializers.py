from rest_framework import serializers
from .models import Author, Presentation


class AuthorSerializer(serializers.ModelSerializer):
    presentations = serializers.StringRelatedField(many=True)  # Отображение названий презентаций

    class Meta:
        model = Author
        fields = ['id', 'fio', 'presentations']


class PresentationSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())  # Если хотите передавать ID

    class Meta:
        model = Presentation
        fields = [
            'id',
            'title',
            'department',
            'creation_date',
            'descript',
            'image_name',
            'file_name',
            'author',
        ]
