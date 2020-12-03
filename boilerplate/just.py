from boilerplate.generator import Generator


class JustGenerator(Generator[int, str]):

    def name(self) -> str:
        return 'JustGenerator'

    def enabled(self, input):
        pass

    def generate(self, input: int) -> str:
        return str(input)
