from tortoise import fields
from tortoise.models import Model

class GardenEntry(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(max_length=50)
    frequency = fields.CharField(max_length=15, null=True)
    watering_period = fields.CharField(max_length=15, null=True)
    time_per_week = fields.CharField(max_length=15, null=True)

    class Meta: 
        table = "Garden"