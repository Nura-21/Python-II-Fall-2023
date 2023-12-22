# Я удалаю те которые выше min(degree)

class MyPolynomial:
    coeffs = []

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __str__(self):
        res = ''
        degree = self.getDegree()
        for i in range(len(self.coeffs)):
            res += f'{self.coeffs[i]}x^{degree - i}'
            if i < degree:
                res += ' + '
        return res

    def __repr__(self):
        return self.__str__

    def toString(self):
        return self.__str__

    def getDegree(self):
        return len(self.coeffs) - 1

    def evaluate(self, x):
        res = 0
        degree = self.getDegree()
        for i in range(len(self.coeffs)):
            res += self.coeffs[i] * (x ** (degree - i))
        return res

    def __add__(self, right):
        degree = self.getDegree()
        right_degree = right.getDegree()
        right_i = min(degree, right_degree)
        max_d = max(degree, right_degree)
        reversed_self = self.coeffs[::-1]
        reversed_right = right.coeffs[::-1]
        for i in range(right_i + 1):
            reversed_self[i] += reversed_right[i]
        coeffs = reversed_self[::-1]
        return MyPolynomial(coeffs)

    def __multiply__(self, right):
        degree = self.getDegree()
        right_degree = right.getDegree()
        right_i = min(degree, right_degree)
        max_d = max(degree, right_degree)
        reversed_self = self.coeffs[::-1]
        reversed_right = right.coeffs[::-1]
        for i in range(right_i + 1):
            reversed_self[i] *= reversed_right[i]
        coeffs = reversed_self[::-1]
        return MyPolynomial(coeffs)

    def add(self, right):
        return self.__add__(right)

    def multiply(self, right):
        return self.__multiply__(right)

    # For other operators same logic


p1 = MyPolynomial([1, 2, 3])
p2 = MyPolynomial([2, 6, 9, 1])
# print(p1.add(p2))
print(p1.evaluate(3))
# print(p2)
