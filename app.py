import matplotlib.pyplot as plt
print("---- Simple Budget Planner ----")
income = int(input("Enter your monthly income: "))
ideal_percentages = {
    "Rent": 0.30,
    "Food & Drinks": 0.15,
    "Health": 0.08,
    "Insurance": 0.07,
    "Savings & Investments": 0.25,
    "Miscellaneous": 0.15}

print("\nNow tell me what you actually spend so we can compare:")

ideal_amounts = {}
for category, pct in ideal_percentages.items():
    ideal_amounts[category] = income * pct

actual_amounts = {}
for category in ideal_percentages.keys():
    actual_amounts[category] = float(input(f"How much do you spend on {category}? ₹"))

print("\n--- Opinion Time ---\n")

for category in ideal_percentages.keys():
    ideal = ideal_amounts[category]
    actual = actual_amounts[category]

    if actual > ideal:
        print(f"You overspend on {category}. Maybe chill a bit there")
    elif actual < ideal * 0.7:
        print(f"You spend pretty low on {category}. Could increase it a bit here and there")
    else:
        print(f"{category} looks balanced 👍")
labels = list(ideal_percentages.keys())
ideal_values = list(ideal_amounts.values())
actual_values = list(actual_amounts.values())

fig1, ax1 = plt.subplots()
ax1.pie(ideal_values, labels=labels, autopct='%1.1f%%')
ax1.set_title("Ideal Budget Split")

fig2, ax2 = plt.subplots()
ax2.pie(actual_values, labels=labels, autopct='%1.1f%%')
ax2.set_title("Your Actual Spending")

plt.show()