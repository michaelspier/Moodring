from django.db import models

# Create your models here.
class Day(models.Model):
    date = models.DateField()
    def __str__(self):
        return str('%d/%d/%d' % (self.date.month, self.date.day, self.date.year))

class Mood(models.Model):
    x_value = models.SmallIntegerField()
    y_value = models.SmallIntegerField()
    description = models.TextField()
    rec_date = models.DateTimeField('date recorded')
    mood_day = models.ForeignKey(Day, default=1, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

class Event_Type(models.Model):
    type_name = models.CharField(max_length=200)
    def __str__(self):
        return self.type_name

class Event(models.Model):
    rec_date = models.DateTimeField('date recorded')
    notes = models.TextField()
    event_type = models.ForeignKey(Event_Type, on_delete=models.CASCADE)
    event_day = models.ForeignKey(Day, default=1, on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.rec_date.month) + "/" + str(self.rec_date.day) + "/" + str(self.rec_date.year))
