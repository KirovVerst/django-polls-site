import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from polls.models import Choice
from polls.models import Question


# Create your tests here.


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], ["<Question: Past question.>"])

    def test_future_question(self):
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_and_future_questions(self):
        create_question(question_text="Future question.", days=30)
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], ["<Question: Past question.>"])

    def test_two_past_questions(self):
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], ["<Question: Past question 2.>", "<Question: Past question 1.>"]
        )


class QuestionDetailViewTests(TestCase):
    def setUp(self) -> None:
        user_password = "temporary"
        user = User.objects.create_user("temporary", "temporary@gmail.com", user_password)
        self.client.login(username=user.username, password="temporary")

    def test_future_question(self):
        future_question = create_question(question_text="Future question.", days=30)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past question.", days=-30)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class ResultsDetailViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question = Question.objects.create(question_text="question text", pub_date=timezone.now())
        cls.choice_1 = Choice.objects.create(choice_text="choice 1", question_id=cls.question.id)
        cls.choice_2 = Choice.objects.create(choice_text="choice 2", question_id=cls.question.id)

    def setUp(self):
        user_password = "temporary"
        self.user = User.objects.create_user("temporary", "temporary@gmail.com", user_password)
        self.client.login(username=self.user.username, password="temporary")

    def test_results_with_no_votes(self):
        response = self.client.get(reverse("polls:results", args=(self.question.id,)))
        self.assertEqual(response.status_code, 200)
        results = self._render_expected_results(0, 0)
        self.assertInHTML(results, response.rendered_content)

    def test_results_with_votes(self):
        self.choice_1.vote_set.create(user=self.user, question=self.question)
        response = self.client.get(reverse("polls:results", args=(self.question.id,)))
        self.assertEqual(response.status_code, 200)
        results = self._render_expected_results(1, 0)
        self.assertInHTML(results, response.rendered_content)

    def _render_expected_results(self, votes_1, votes_2):
        return f"""
<tr>
   <td>{self.choice_1.choice_text}</td>
   <td>{votes_1}</td>
</tr>
<tr>
   <td>{self.choice_2.choice_text}</td>
   <td>{votes_2}</td>
</tr>
""".strip()
