from plantilla_chatbot.analyse.abc import Validator
from plantilla_chatbot.analyse.decorators import test


class RegexValidator(Validator):
    def __init__(self, comment: str) -> None:
        super(RegexValidator, self).__init__(comment)


class LengthValidator(Validator):
    def __init__(self, comment: str):
        super(LengthValidator, self).__init__(comment)

    @test()
    def _count_lines(self) -> bool:
        return len(self.comment) > 3 and len(self.comment) <= 7
