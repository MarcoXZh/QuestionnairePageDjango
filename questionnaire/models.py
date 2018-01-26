from django.db import models
import json

class Question(models.Model):
    '''
    The questions
    '''
    text = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return 'Question<%d>: %s' % (self.id, self.text)
    # def __str__(self)
# class Question(models.Model)


class Questioner(models.Model):
    '''
    The people providing answers
    '''
    name = models.CharField(max_length=256, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    answers = models.CharField(max_length=4096)

    def __str__(self):
        return 'Questioner<%s>: %s - answers=%d' % \
                    (self.date, self.name, len(json.loads(self.answers).items()))
    # def __str__(self)
# class Questioner(models.Model)