from rest_framework import serializers
from .models import Todo


class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title')

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description')

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created_date')