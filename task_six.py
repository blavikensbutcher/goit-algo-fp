items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):

    chosen = []

    total_calories = 0


    item_list = []
    for name in items:
        cost = items[name]["cost"]
        cal = items[name]["calories"]
        ratio = cal / cost 
        item_list.append((name, cost, cal, ratio))


    item_list.sort(key=lambda x: x[3], reverse=True)


    for name, cost, cal, _ in item_list:
        if cost <= budget:
            chosen.append(name)
            total_calories += cal
            budget -= cost

    return chosen, total_calories

def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)


    dp = [[0] * (budget + 1) for _ in range(n + 1)]


    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        cal = items[name]["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + cal)
            else:
                dp[i][b] = dp[i - 1][b]


    res = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            res.append(name)
            b -= items[name]["cost"]

    total_calories = dp[n][budget]
    return res[::-1], total_calories  



budget = 100

print("Жадібний алгоритм:")
chosen_greedy, cal_greedy = greedy_algorithm(items, budget)
print("Страви:", chosen_greedy)
print("Калорій:", cal_greedy)

print("\nДинамічне програмування:")
chosen_dp, cal_dp = dynamic_programming(items, budget)
print("Страви:", chosen_dp)
print("Калорій:", cal_dp)