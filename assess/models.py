from django.db import models
from django.core.validators import MaxValueValidator

class Criteria(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    weight = models.IntegerField(default=0, validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.name

    def get_ordered_list(self):
        return self.objects.all().order_by('name')

class Rating(models.Model):
    pseudonim = models.CharField(max_length=60)
    link = models.TextField()
    rating = models.FloatField()
    is_ready = models.BooleanField()
    creterias = models.ManyToManyField(Criteria, through='Marks')

    def __str__(self):
        return self.pseudonim

    def get_all_marks(self):
        marks_list = []
        for crit in Criteria.objects.all():
            mark = Marks.objects.get(pseudonim=self, weight = crit)
            marks_list.append(mark)
        return marks_list

    @property
    def calc_rating(self):
        rating = 0
        for crit in Criteria.objects.all():
            mark = Marks.objects.get(pseudonim=self, weight=crit)
            rating+=mark.value*crit.weight
        self.rating = rating
        return rating

class Marks(models.Model):
    pseudonim = models.ForeignKey(Rating, on_delete=models.CASCADE)
    weight = models.ForeignKey(Criteria,  on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    def __str__(self):
        return ('%s - %s - %s' % (self.pseudonim, self.weight, self.value))
