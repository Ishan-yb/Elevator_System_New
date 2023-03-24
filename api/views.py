from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import *
from api.models import Elevator
from django.http import JsonResponse


# Create your views here.


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=False, methods=['POST', 'GET'])
    def initialize(self, request, pk=None):
        if request.method == 'GET':
            queryset = Elevator.objects.all()
            serializers_data = ElevatorSerializer(queryset, many=True, context={'request': request})
            return Response(serializers_data.data)
        if request.method != 'POST':
            pass
        else:
            number_of_elevator = request.data.get('n', 0)
        if number_of_elevator <= 0:
            return Response({"error": "Number Elevator should be greater than 0"}, status=400)

        elevators = []
        for i in range(number_of_elevator):
            elevators.append(Elevator())
        elevator_data = []
        for e in elevators:
            elevator_data.append(
                {'elevator_id': e.elevator_id, 'availability': e.availability, 'direction': e.direction,
                 'current_floor': e.current_floor, 'destination_floor': e.destination_floor,
                 'status': e.status})
        serializer_class_custom = ElevatorSerializer(data=elevator_data, many=True, context={'request': request})

        if serializer_class_custom.is_valid():
            serializer_class_custom.save()
            return JsonResponse(serializer_class_custom.data, safe=False, status=202)
        return JsonResponse({"error": serializer_class_custom.errors}, status=400)

    @action(detail=True, methods=['GET'])
    def next_destination(self, request, pk=None):
        try:
            target_elevator = Elevator.objects.get(pk=pk)
        except Elevator.DoesNotExist:
            return Response({"error": "Elevator does not exist"}, status=400)

        serializers_data = ElevatorSerializer(target_elevator, context={'request': request})
        return Response({"destination_floor": serializers_data.data["destination_floor"]}, status=201)

    @action(detail=True, methods=['GET'])
    def get_direction(self, request, pk=None):
        try:
            target_elevator = Elevator.objects.get(pk=pk)
        except Elevator.DoesNotExist:
            return Response({"error": "Elevator does not exist"}, status=400)

        serializers_data = ElevatorSerializer(target_elevator, context={'request': request})

        if serializers_data.data["destination_floor"] > serializers_data.data["current_floor"]:
            target_elevator.direction = "UP"
            target_elevator.save()
            return Response({"Direction": "UP"}, status=201)
        target_elevator.direction = "DOWN"
        target_elevator.save()
        return Response({"Direction": "DOWN"}, status=201)

    @action(detail=True, methods=['GET'])
    def get_elevator_request_list(self, request, pk=None):
        try:
            target_elevator = Elevator.objects.get(pk=pk)
        except Elevator.DoesNotExist:
            return Response({"error": "Elevator does not exist"}, status=400)
        try:
            req = Request.objects.filter(elevator=target_elevator)
        except Request.DoesNotExist:
            return Response({"error": "Request for this elevator does not exist"}, status=400)
        req_serializer = RequestSerializer(req, many=True, context={"request": request})
        return Response(req_serializer.data)

    @action(detail=True, methods=['GET', 'PATCH'])
    def getting_lift_request(self, request, pk=None):
        try:
            target_elevator = Elevator.objects.get(pk=pk)
        except Elevator.DoesNotExist:
            return Response({"error": "Elevator does not exist"}, status=400)

        if request.method == 'GET':
            serializers_data = ElevatorSerializer(target_elevator, context={'request': request})
            return Response(serializers_data.data)
        if request.method != 'PATCH':
            pass
        try:
            target_elevator = Elevator.objects.get(pk=pk)
        except Elevator.DoesNotExist:
            return Response({"error": "Elevator does not exist"}, status=400)
        try:
            req = Request.objects.filter(elevator=target_elevator)
        except Request.DoesNotExist:
            return Response({"error": "Request for this elevator does not exist"}, status=400)
        if len(req) == 0:
            return Response({"Response": "Response list is empty"}, status=400)
        req_list = req[::-1]
        req_obj = req_list.pop()

        if target_elevator.destination_floor == req_obj.request_floor:
            target_elevator.current_floor = target_elevator.destination_floor
            target_elevator.destination_floor = req_obj.floor_number
            req_obj.delete()
        if target_elevator.current_floor != req_obj.request_floor:
            req_list.append(req_obj)
            target_elevator.current_floor = target_elevator.destination_floor
            target_elevator.destination_floor = req_obj.request_floor
        target_elevator.save()
        return JsonResponse({"Response": "Updated the elevator destination"}, status=202)


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer








