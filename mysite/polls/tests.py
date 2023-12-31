import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

class QuestionModelTests(TestCase):
    '''
    Here we have created a subclass with a method that creates a question instance with a pub_date in the future we then check the output of was published recently which ought to be False
    '''
    def test_was_published_recently_with_future_question(self):
        '''
        was published recently() returns False for questions whose pub_date is in the future
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        
        # Was published recently() returns False for questions whose pub_date is in the older than 1 day
        
        time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        # Was published recently() returns True for questions whose pub date is within the last day
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds= 59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
        