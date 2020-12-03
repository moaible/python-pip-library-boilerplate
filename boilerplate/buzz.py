from .generator import Generator

class BuzzGenerator(Generator[int, str]):

    def __init__(self):
        pass

    def name(self) -> str:
        return "BuzzGenerator"

    def enabled(self, input):
        return input % 5 == 0

    def generate(self, input: int) -> str:
        return "Buzz"
