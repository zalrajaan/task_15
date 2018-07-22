from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
        	'name',
        	'opening_time',
        	'closing_time',
        	]

class Anything2(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'owner', 'name', 'description', 'opening_time','closing_time']

class Anything3(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name','description', 'opening_time','closing_time']

class Anything4(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
