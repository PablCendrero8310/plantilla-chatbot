# analyse/validators.py
import re

import plantilla_chatbot.filters.regex as patterns
from plantilla_chatbot.analyse.abc import Tests
from plantilla_chatbot.analyse.decorators import test


class RegexTests(Tests):
    """
    Pruebas para comprobar expresiones regulares propias de peticiones escritas con IA.
    """

    @test()
    def pvn_test(self):
        return bool(
            re.search(
                pattern=patterns.PVN_REGEX,
                string=self.comment,
                flags=re.IGNORECASE | re.VERBOSE,
            )
        )


class LengthTests(Tests):
    "Pruebas para comprobar patrones de longitud comunes en mensajes escritos con IA."

    @test()
    def _count_lines(self) -> bool:
        return 7 >= len(self.comment_lines) > 3

    @test(weight=0.5)
    def _count_first_line(self) -> bool:
        return 4 <= len(self.comment_lines[0].strip()) <= 5
