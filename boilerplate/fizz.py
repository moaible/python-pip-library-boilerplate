from boilerplate.generator import Generator

class FizzGenerator(Generator[int, str]):

    def name(self) -> str:
        return "FizzGenerator"

    def enabled(self, input):
        return input % 3 == 0

    def generate(self, input: int) -> str:
        return "Fizz"
