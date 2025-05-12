import random
from collections import Counter

def roll_dice_once(m, n):
    return sum(random.randint(1, n) for _ in range(m))

def simulate_rolls(m, n, k):
    return [roll_dice_once(m, n) for _ in range(k)]

def calculate_distribution(results, total_rolls):
    counter = Counter(results)
    return {total: count / total_rolls for total, count in counter.items()}

