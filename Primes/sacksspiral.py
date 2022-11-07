import numpy as np
from prime import is_prime

class SacksSpiral:
    def __init__(self, size):
        self.size = size
        self.max_num = self.size ** 2
        self.arr = np.zeros((2 * self.size, 2 * self.size, 3))
        self.primes41 = {i ** 2 + i + 41 for i in range(1000) if is_prime(i ** 2 + i + 41)}
        self.primes17 = {i ** 2 + i + 17 for i in range(1000) if is_prime(i ** 2 + i + 17)}
        self.primes11 = {i ** 2 + i + 11 for i in range(1000) if is_prime(i ** 2 + i + 11)}

    def get_index(self, num):
        rho = np.sqrt(num)
        phi = 2 * np.pi * rho
        row = int(rho * np.sin(phi)) + self.size
        col = int(rho * np.cos(phi)) + self.size
        return row, col

    def get_spiral(self):
        for num in range(self.max_num):
            if num in self.primes41 and is_prime(num):
                index = self.get_index(num)
                self.arr[index] = (255, 0, 0)
            elif num in self.primes17 and is_prime(num):
                index = self.get_index(num)
                self.arr[index] = (0, 255, 0)
            elif num in self.primes11 and is_prime(num):
                index = self.get_index(num)
                self.arr[index] = (0, 0, 255)
            elif is_prime(num):
                index = self.get_index(num)
                self.arr[index] = (255, 255, 255)
        return np.rot90(self.arr, -1)