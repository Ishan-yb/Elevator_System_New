from django.db import models


# Create your models here.
class Elevator(models.Model):
    elevator_id = models.AutoField(primary_key=True)
    current_floor = models.IntegerField(default=0)
    destination_floor = models.IntegerField(default=0)
    direction = models.CharField(max_length=10, default='stop')
    status = models.CharField(max_length=20, default='working')
    availability = models.BooleanField(default=True)

    def __int__(self):
        return self.elevator_id


class Floor(models.Model):
    floor_number = models.IntegerField(primary_key=True, default=0)
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE, null=True)


class Request(models.Model):
    floor_number = models.IntegerField(default=0)
    direction = models.CharField(max_length=10, default='up')
    timestamp = models.DateTimeField(auto_now_add=True)
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE, null=True)
