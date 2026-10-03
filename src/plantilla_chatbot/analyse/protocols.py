# analyse/protocols.py
from typing import Protocol


class Test(Protocol):
    """
    Define el contrato de una función ejecutora de una prueba.
    """

    __test_weight__: float

    def __call__(self) -> bool: ...
