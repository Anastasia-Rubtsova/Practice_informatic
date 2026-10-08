import random

def birthday_probability(people):
    if people > 365:
        return 1.0
    if people <= 1:
        return 0.0
    prob = 1.0
    for i in range(people):
        prob = prob * (365 - i) / 365
    return 1.0 - prob

def simulate_birthday(people, trials):
    successes = 0
    for i in range(trials):
        birthdays = []
        for j in range(people):
            birthdays.append(random.randint(1, 365))
        if len(set(birthdays)) < people:
            successes = successes + 1
    return successes / trials
