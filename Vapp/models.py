from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=200)
    from_where = models.CharField(max_length=200)
    to_where = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    freight = models.FloatField(default=0)
    acceptance = models.CharField(max_length=7,blank=True)

    def __str__(self):
        return self.name