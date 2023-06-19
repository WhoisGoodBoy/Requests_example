class Donkey:
    strength = 50

    @classmethod
    def print_strength(cls):
        print(cls, cls.strength)


class Horse:
    speed = 5

    @classmethod
    def print_strength(cls):
        print(cls, cls.speed)


class Mul(Horse, Donkey):
    pass

mul = Mul()
mul.print_strength()