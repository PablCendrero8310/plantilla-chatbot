# analyse/validators.py
import re

import plantilla_chatbot.filters.patterns as patterns
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

    @test()
    def reliable_source_test(self):
        return bool(
            re.search(
                pattern=patterns.RELIABLE_SOURCE_REGEX,
                string=self.comment,
                flags=re.IGNORECASE | re.VERBOSE,
            )
        )

    @test()
    def relevance_test(self):
        return bool(
            re.search(
                pattern=patterns.RELEVANCE_REGEX,
                string=self.comment,
                flags=re.IGNORECASE | re.VERBOSE,
            )
        )

    @test()
    def coi_test(self):
        return bool(
            re.search(
                pattern=patterns.COI_REGEX,
                string=self.comment,
                flags=re.IGNORECASE | re.VERBOSE,
            )
        )
