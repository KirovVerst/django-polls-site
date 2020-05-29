from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from polls.models import Choice
from polls.models import Question
from polls.services import VoteService


class VoteServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user("temporary", "temporary@gmail.com", "temporary")
        cls.question = Question.objects.create(question_text="question text", pub_date=timezone.now())
        cls.choice_1 = Choice.objects.create(choice_text="choice 1", question_id=cls.question.id)
        cls.choice_2 = Choice.objects.create(choice_text="choice 2", question_id=cls.question.id)
        cls.service = VoteService(cls.user)

    def test_vote(self):
        self.service.vote(self.question, self.choice_1.id)

        self.assertEqual(self.choice_1.votes_count(), 1)
        self.assertEqual(self.choice_1.votes_set.first().user, self.user)

        self.assertEqual(self.choice_2.votes_count(), 0)

    def test_update_vote(self):
        self.service.vote(self.question, self.choice_1.id)
        self.assertEqual(self.choice_1.votes_count(), 1)

        self.service.vote(self.question, self.choice_2.id)
        self.assertEqual(self.choice_2.votes_count(), 1)
        self.assertEqual(self.choice_1.votes_count(), 0)
