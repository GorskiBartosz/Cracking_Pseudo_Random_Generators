class GlibcRandom:
    def __init__(self, seed, a, m):
        self.generated_numbers = list()
        self.generated_numbers.append(seed)
        self.a = a
        self.m = m

        for i in range(0, 30):
            self.generated_numbers.append(self.m * self.generated_numbers[i] % self.m)
        for i in range(0, 3):
            self.generated_numbers.append(self.generated_numbers[i])
        for i in range(0, 310):
            self.get_next_int()

    def get_next_int(self):
        i = len(self.generated_numbers)
        self.generated_numbers.append(self.generated_numbers[i - 31] + self.generated_numbers[i - 3])
        return self.generated_numbers[i] >> 1


def recognize_glibc_random(generator):
    retrieved_numbers = list()
    for i in range(0, 31):
        retrieved_numbers.append(generator.get_next_int())

    for i in range(0, 20):
        x1 = retrieved_numbers[i]
        x2 = retrieved_numbers[i + 28]
        # there are two possible outputs
        # 1. x1 or/and x2 was even so the possible parity bit will be ommited in result
        first_possibility = (x1 * 2 + x2 * 2) >> 1
        # 2. x1 and x2 ware both odd
        second_possibility = ((x1 * 2 + 1) + (x2 * 2 + 1)) >> 1
        new_generated_num = generator.get_next_int()
        if first_possibility != new_generated_num and second_possibility != new_generated_num:
            return False
        retrieved_numbers.append(new_generated_num)
    return True
