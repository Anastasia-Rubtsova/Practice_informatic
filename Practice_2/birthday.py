import random

def birthday_probability(people):
    if people > 365:
        return 1.0
    if people <= 1:
        return 0.0
    
    prob_all_different = 1.0
    days_in_year = 365
    
    for i in range(people):
        prob_all_different *= (days_in_year - i) / days_in_year
    
    return 1 - prob_all_different


def simulate_birthday(people, trials):
    successes = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(set(birthdays)) < people:
            successes += 1
    return successes / trials


people = int(input("Введите число людей: "))
trials = int(input("Введите число симуляций: "))

exact = birthday_probability(people)
simulated = simulate_birthday(people, trials)

print(f"Точная вероятность совпадения: {exact:.4f}")
print(f"Симуляционная оценка ({trials} испытаний): {simulated:.4f}")

# Поиск порога > 50%
for n in range(1, 100):
    if birthday_probability(n) > 0.5:
        print(f"Наименьшее число людей с вероятностью > 50%: {n}")
        break
