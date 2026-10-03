# analyse/validators.py
from plantilla_chatbot.analyse.abc import Tests
from plantilla_chatbot.analyse.decorators import test


class RegexTests(Tests):
    """
    Pruebas para comprobar expresiones regulares propias de peticiones escritas con IA.
    """

    pass


class LengthTests(Tests):
    "Pruebas para comprobar patrones de longitud comunes en mensajes escritos con IA."

    @test()
    def _count_lines(self) -> bool:
        return len(self.comment) > 3 and len(self.comment) <= 7
