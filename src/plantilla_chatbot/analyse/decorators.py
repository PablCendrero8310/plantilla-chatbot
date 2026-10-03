from collections.abc import Callable
from typing import cast

from plantilla_chatbot.analyse.protocols import Test


def test(weight: float = 1.0):
    def decorator(func: Callable[..., bool]) -> Test:
        result = cast(Test, func)
        result.__test_weight__ = weight
        return result

    return decorator
