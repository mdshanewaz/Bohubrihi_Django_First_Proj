from django.db import models

# Create your models here.

# CREATE TABLE Person(
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL,
# );

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    
    rating = (
        (1, "Best"),
        (2, "Better"),
        (3, "Good"),
        (4, "Bad"),
        (5, "Worst"),
    )

    num_stars = models.IntegerField(choices = rating)

    def __str__(self):
        return self.name + ", Ratting : " + str(self.num_stars)

    