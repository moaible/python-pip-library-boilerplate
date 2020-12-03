from .generator import Generator

class JustGenerator(Generator[int, str]):

    def __init__(self):
        pass

    def name(self) -> str:
        return "JustGenerator"

    def enabled(self, input):
        pass

    def generate(self, input: int) -> str:
        return str(input)
