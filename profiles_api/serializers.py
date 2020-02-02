from rest_framework import serializers

class HelloSeializers(serializers.Serializer):
    """Serializer a name field for testing our API View"""
    name = serializers.CharField(max_length=10)