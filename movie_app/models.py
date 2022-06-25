from django.db.models import Sum
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


STAR_CHOICE = (
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "****"),
    (5, "*****"),
)


class Review(models.Model):
    text = models.TextField(max_length=250)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=STAR_CHOICE, null=True, default=1)

    def __str__(self):
        return self.text

    @property
    def rating(self):
        s = Review.objects.all().aggregate(Sum("stars"))["stars__sum"]
        c = Review.objects.all().count()
        try:
            return s / c
        except:
            return 0


# Create your models here.
