# analyse/abc.py
from typing import List

from plantilla_chatbot.analyse.protocols import Test


class Tests:
    """Clase base para implementar pruebas de comentarios.

    Proporciona el separador del comentario en lineas mediante el constructor y la función ``score`` para obtener la puntuación.
    """

    comment: str
    comment_lines: List[str]

    def __init__(self, comment: str) -> None:
        self.comment = comment
        self.comment_lines = [line for line in comment.splitlines() if line != ""]

    def score(self) -> float:
        """Función para obtener el resultado de las pruebas obtenido mediante sumar el resultado de cada prueba y dividirlo entre el puntaje máximo.

        Returns:
            El resultado de la prueba."""
        tests = self._get_tests()
        total_weight = sum(test.__test_weight__ for test in tests)

        if total_weight == 0:
            return 0.0
        # Get the result
        score = sum(test.__test_weight__ for test in tests if test())

        return score / total_weight

    def _get_tests(self) -> list[Test]:
        # Obtiene todas las funciones con peso capaces de ejecutar una prueba.
        return [
            getattr(self, name)
            for name in dir(self)
            if getattr(getattr(self, name), "__test_weight__", None) is not None
        ]
