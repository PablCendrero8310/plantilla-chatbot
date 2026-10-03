from abc import ABC, abstractmethod


class Validator(ABC):
    def __init__(self, comment: str) -> None:
        self.comment = [line for line in comment.splitlines() if line != ""]

    @abstractmethod
    def score(self) -> int:
        pass
