from django.db import models
from django.core.validators import MaxValueValidator

class Criteria(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    weight = models.IntegerField(default=0, validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.name

class Rating(models.Model):
    pseudonim = models.CharField(max_length=60)
    link = models.TextField()
    rating = models.FloatField()
    is_ready = models.BooleanField()
    creterias = models.ManyToManyField(Criteria, through='Marks')

    def __str__(self):
        return self.pseudonim

class Marks(models.Model):
    pseudonim = models.ForeignKey(Rating, on_delete=models.CASCADE)
    weight = models.ForeignKey(Criteria,  on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    def __str__(self):
        return ('%s - %s - %s' % (self.pseudonim, self.weight, self.value))
