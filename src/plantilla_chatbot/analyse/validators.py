from plantilla_chatbot.analyse.abc import Validator
from plantilla_chatbot.analyse.decorators import test


class RegexValidator(Validator):
    pass


class LengthValidator(Validator):
    @test()
    def _count_lines(self) -> bool:
        return len(self.comment) > 3 and len(self.comment) <= 7
