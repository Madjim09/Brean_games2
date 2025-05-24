import random
import math

RULE = "Find the smallest common multiple of given numbers."

def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    lcm = abs(num1 * num2) // math.gcd(num1, num2)
    return question, str(lcm)