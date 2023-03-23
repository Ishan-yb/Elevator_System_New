from rest_framework import serializers
from .models import Elevator, Floor, Request


class ElevatorSerializer(serializers.ModelSerializer):
    elevator_id = serializers.ReadOnlyField()

    class Meta:
        model = Elevator
        fields = '__all__'


class FloorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Request
        fields = '__all__'
