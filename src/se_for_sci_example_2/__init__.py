import dataclasses

@dataclasses.dataclass(frozen=True)
class Vector:
    x: float
    y: float

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def mag(self):
        return (self.x**2 + self.y**2) ** 0.5


def main() -> None:
    print("Hello from se-for-sci-example-2!")
