import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(39))