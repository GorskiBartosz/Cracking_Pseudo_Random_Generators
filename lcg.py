import math
from functools import reduce


class LCG:
    def __init__(self, seed, a, c, m):
        self.last_number = seed
        self.a = a
        self.c = c
        self.m = m

    def get_next_int(self):
        self.last_number = (self.last_number * self.a + self.c) % self.m
        return self.last_number


def try_to_find_unknown_m(numbers):
    diffs = [s1 - s0 for s0, s1 in zip(numbers, numbers[1:])]
    zeroes = [t2 * t0 - t1 * t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    return abs(reduce(math.gcd, zeroes))


def try_to_retrieve_lcg_parameters(generator):
    random_numbers = list()
    random_numbers.append(generator.get_next_int())
    random_numbers.append(generator.get_next_int())
    random_numbers.append(generator.get_next_int())
    random_numbers.append(generator.get_next_int())
    random_numbers.append(generator.get_next_int())
    random_numbers.append(generator.get_next_int())
    m = try_to_find_unknown_m(random_numbers)
    a = find_unknown_a(random_numbers, m)
    c = find_unknown_c(random_numbers, a, m)
    return a, c, m


def find_next_number(numbers, a, c, m):
    assert len(numbers) >= 1
    return (numbers[len(numbers) - 1] * a + c) % m


def find_unknown_c(numbers, a, m):
    assert len(numbers) >= 3
    return (numbers[2] - (a * numbers[1])) % m


def find_inverse_for_x_in_m_ring(x, m):
    d, _, y = egcd(m, x)
    assert d == 1
    return y


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = egcd(b, a % b)
        d, x, y = d, y, x - (math.floor(a / b) * y)
        return d, x, y


def find_unknown_a(numbers, m):
    assert len(numbers) >= 4
    divider = (numbers[0] - numbers[1])
    divider_inverse = find_inverse_for_x_in_m_ring(divider, m)
    return ((numbers[1] - numbers[2]) * divider_inverse) % m


def predict_next_lgc_value(last, a, c, m):
    return (last * a + c) % m


# returns true if given generator is an instance of LGC
def recognize_lgc(generator):
    for i in range(1, 1000):
        try:
            a, c, m = try_to_retrieve_lcg_parameters(generator)
            generated_num = generator.get_next_int()
            for j in range(1, 20):
                predicted_num = predict_next_lgc_value(generated_num, a, c, m)
                generated_num = generator.get_next_int()
                assert (generated_num == predicted_num)

            return True
        except AssertionError:
            pass
    return False
