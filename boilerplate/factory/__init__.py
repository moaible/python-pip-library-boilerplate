from boilerplate.generator import Generator
from typing import TypeVar, Generic, Callable, List

I = TypeVar("I")
O = TypeVar("O")

class Factory(Generic[I, O]):

    def __init__(self, 
        generators: List[Generator[I, O]], 
        fallback: Generator[I, O],
        reducer: Callable[[List[O]], O]):
            self.generators = generators
            self.fallback = fallback
            self.reducer = reducer
    
    def create(self, input: I) -> O:
        available_generators = [generator 
            for generator in self.generators 
            if generator.enabled(input)]
        if len(available_generators) == 0:
            return self.fallback.generate(input)
        values = [gen.generate(input) for gen in available_generators]
        return self.reducer(values)
