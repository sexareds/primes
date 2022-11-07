import numpy as np
from prime import is_prime

class UlamSpiral:
    def __init__(self, size):
        self.size = size if size % 2 else size + 1
        self.max_num = self.size ** 2
        self.arr = np.zeros((self.size, self.size, 3))
        self.pos = np.array([self.size, self.size]) // 2
        self.step = 1
        self.num = 1
        self.primes41 = {i ** 2 + i + 41 for i in range(1000) if is_prime(i ** 2 + i + 41)}
        self.primes17 = {i ** 2 + i + 17 for i in range(1000) if is_prime(i ** 2 + i + 17)}
        self.primes11 = {i ** 2 + i + 11 for i in range(1000) if is_prime(i ** 2 + i + 11)}

    def fill_side(self, iterations, side):
        for i in range(iterations):
            if self.num == self.max_num:
                break
            if self.num in self.primes41:
                self.arr[self.pos[1], self.pos[0]] = (255, 0, 0)
            elif self.num in self.primes17:
                self.arr[self.pos[1], self.pos[0]] = (0, 255, 0)
            elif self.num in self.primes11:
                self.arr[self.pos[1], self.pos[0]] = (0, 0, 255)
            else:
                self.arr[self.pos[1], self.pos[0]] = [255] * 3 if is_prime(self.num) else [0] * 3
            self.pos[side] += self.step if self.step else -self.step
            self.num += 1
        self.step *= -1

    def get_spiral(self):
        for iterations in range(1, self.size * self.size):
            self.fill_side(iterations, 0)
            self.fill_side(iterations, 1)
            self.step *= -1
        return np.rot90(np.flip(self.arr, axis=0), -1)