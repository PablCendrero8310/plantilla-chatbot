from typing import Protocol


class Test(Protocol):
    __test_weight__: float

    def __call__(self) -> bool: ...
