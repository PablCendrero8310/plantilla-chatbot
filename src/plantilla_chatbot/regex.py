import re

from plantilla_chatbot.validator import Validator


class RegexValidator(Validator):
    comment: str

    def __init__(self, comment: str) -> None:
        self.comment = comment

    def score(self) -> int:
        return 0
