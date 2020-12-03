from abc import ABCMeta
from abc import abstractmethod
from typing import TypeVar, Generic

I = TypeVar('I')
O = TypeVar('O')


class Generator(Generic[I, O], metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def enabled(self, input: I) -> bool:
        pass

    @abstractmethod
    def generate(self, input: I) -> O:
        pass
