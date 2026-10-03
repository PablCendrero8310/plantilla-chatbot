from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def score(self) -> int:
        pass
