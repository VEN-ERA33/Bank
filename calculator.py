class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return Calculator(self.value / other.value)
        else:
            raise ValueError("Деление на ноль невозможно.")

    def __str__(self):
        return str(self.value)
