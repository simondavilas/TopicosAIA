from django.db import models

data_sets = [("", "Selecciona uno"), ("cover_type", "Cover type")]


class DataSet(models.Model):

    conjunto_de_datos = models.TextField(null=False, blank=False, choices=data_sets, max_length=100, name="conjunto_de_datos")

    def __str__(self) -> str:
        return self.conjunto_de_datos
    
class TrainSet(models.Model):

    modelos = models.TextField(null=False, blank=False, choices=data_sets, max_length=100, name="modelos")

    def __str__(self) -> str:
        return self.modelos
    
class InferenceModel(models.Model):

    elevation = models.Field(null=False, blank=False, default=2991)
    slope = models.Field(null=False, blank=False, default=7)
    horizontal_distance_to_hidrology = models.Field(null=False, blank=False, default=67)
    vertical_distance_to_hidrology = models.Field(null=False, blank=False, default=11)
    horizontal_distance_to_roadways = models.Field(null=False, blank=False, default=1015)
    hillshade_9_am = models.Field(null=False, blank=False, default=233)
    hillshade_noon = models.Field(null=False, blank=False, default=234)
    horizontal_distance_to_firepoints = models.Field(null=False, blank=False, default=1570)
    wilderness_area = models.Field(null=False, blank=False, default=1)
