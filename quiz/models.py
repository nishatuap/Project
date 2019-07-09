from django.db import models

class Questions(models.Model):
    CAT_CHOICES = (
    ('sports','1.Sports'),
    ('movies','2.Movies'),
    ('maths','3.Maths'),
    ('generalknowledge','4.GeneralKnowledge')
    )
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.CharField(max_length=20, choices = CAT_CHOICES)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question
