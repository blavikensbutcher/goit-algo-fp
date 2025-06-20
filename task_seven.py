import random
import matplotlib.pyplot as plt

# Кількість симуляцій
total_rolls = 100000

# Словник для зберігання частоти випадання кожної суми
sums = {i: 0 for i in range(2, 13)}

# Симуляція кидання двох кубиків
for _ in range(total_rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    result = die1 + die2
    sums[result] += 1

# Обчислення ймовірностей
monte_carlo_probs = {s: round((count / total_rolls) * 100, 2) for s, count in sums.items()}

# Аналітичні ймовірності
analytical_probs = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

# Вивід результатів
print("Сума | Монте-Карло (%) | Аналітична (%)")
print("-----------------------------------------")
for s in range(2, 13):
    print(f"{s:>4} | {monte_carlo_probs[s]:>15} | {analytical_probs[s]:>13}")

# Побудова графіка
x = list(range(2, 13))
monte_values = [monte_carlo_probs[i] for i in x]
analytical_values = [analytical_probs[i] for i in x]

plt.plot(x, monte_values, marker='o', label='Монте-Карло')
plt.plot(x, analytical_values, marker='x', label='Аналітична')
plt.title("Ймовірності сум при киданні двох кубиків")
plt.xlabel("Сума")
plt.ylabel("Ймовірність (%)")
plt.legend()
plt.grid(True)
plt.show()