from django.db import models

# Create your models here.


CURRENCY_CHOICES = (
    ('EUR', 'EUROPEAN CURRENCY'),
    ('USD', 'UNITED STATES DOLLAR'),
    ('RUB', 'RUSSIAN ROUBLE'),
    ('YEN', 'JAPAN CURRENCY'),
    ('DIR', 'ARABIAN CURRENCY'),
    ('CAD', 'CANADIAN CURRENCY'),
    
)
class Currency(models.Model):
    currency = models.CharField(max_length=150,choices=CURRENCY_CHOICES)
    
                                

class Course(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    course = models.FloatField()    