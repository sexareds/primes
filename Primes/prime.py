def is_prime(num):
    if num == 2: return True
    if num < 2 or not num % 2: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if not num % i:
            return False
    return True