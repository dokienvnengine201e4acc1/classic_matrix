import random

def matrix():
    while True:
        row = [str(random.randint(0, 1)) for _ in range(200)]
        print(''.join(row))

matrix()
