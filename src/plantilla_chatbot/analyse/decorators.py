# analyse/decorators.py
from collections.abc import Callable
from typing import TypeVar, cast

from plantilla_chatbot.analyse.protocols import Test

F = TypeVar("F", bound=Callable[..., bool])


def test(weight: float = 1.0) -> Callable[[F], Test]:
    """
    Marca una función como ejecutora de una prueba y le asigna un peso.

    Args:
        weight: importancia que tendrá la prueba en el cómputo de la puntuación.

    Returns:
        Un decorador que registra la función como ejecutora de una prueba.
    """

    def decorator(func: Callable[..., bool]) -> Test:
        result = cast(Test, func)
        result.__test_weight__ = weight
        return result

    return decorator
