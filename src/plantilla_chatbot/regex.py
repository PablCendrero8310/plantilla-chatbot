import re


class RegexValidator:
    comment: str

    def __init__(self, comment: str) -> None:
        self.comment = comment

    @property
    def score(self) -> int:
        pass
