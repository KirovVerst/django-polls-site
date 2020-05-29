from django.contrib.auth.models import User

from .models import Choice
from .models import Question
from .models import Votes


class VoteService:
    def __init__(self, user: User):
        self.user = user

    def vote(self, question: Question, choice_pk: int) -> None:
        choice: Choice = question.choice_set.get(pk=choice_pk)
        current_vote: Votes = question.votes_set.filter(user=self.user).first()

        if current_vote:
            current_vote.choice = choice
            current_vote.save()
        else:
            question.votes_set.create(user=self.user, choice=choice)
