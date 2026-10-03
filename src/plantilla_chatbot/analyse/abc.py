from typing import List

from plantilla_chatbot.analyse.protocols import Test


class Validator:
    comment: List[str]

    def __init__(self, comment: str) -> None:
        self.comment = [line for line in comment.splitlines() if line != ""]

    def score(self) -> float:
        # Get tests
        tests = self._get_tests()
        total_weight = sum(test.__test_weight__ for test in tests)

        if total_weight == 0:
            return 0.0

        score = sum(test.__test_weight__ for test in tests if test())
        return score / total_weight

    def _get_tests(self) -> list[Test]:
        return [
            getattr(self, name)
            for name in dir(self)
            if getattr(getattr(self, name), "__test_weight__", None) is not None
        ]
