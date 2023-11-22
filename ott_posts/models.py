from django.db import models
from django.contrib.auth.models import User


class Ott(models.Model):
    NETFLIX = 'Netflix'
    TVING = 'Tving'
    DISNEY = 'Disney+'
    WAVE = 'Wave'
    COUPANGPLAY = 'coupangplay'

    TYPE_CHOICES = [
        (NETFLIX, 'Netflix'),
        (TVING, 'Tving'),
        (DISNEY, 'Disney+'),
        (WAVE, 'Wave'),
        (COUPANGPLAY, 'coupangplay')
    ]
    
    PEOPLE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='Netflix')
    bill = models.IntegerField()
    people = models.IntegerField(choices=PEOPLE_CHOICES, default='1')
    description_OTT = models.TextField(blank=True)

    def __str__(self):
        return f"[{self.type}] {self.people}명 모집중"
