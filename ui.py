from dice_simulator import roll_dice_once, simulate_rolls, calculate_distribution

def run_simulation():
    print("🎲 Dice Probability Simulator 🎲")
    try:
        n = int(input("Enter number of sides on each die (N): "))
        m = int(input("Enter number of dice to roll (M): "))
        k = int(input("Enter number of simulations (K): "))

        if n <= 0 or m < 0 or k <= 0:
            print("❗ Please enter only positive numbers.")
            return

        results = simulate_rolls(m, n, k)
        distribution = calculate_distribution(results, k)

        print("\nProbability Distribution:")
        for total in sorted(distribution):
            print(f"Sum {total}: {distribution[total]:.4f}")
    except ValueError:
        print("❗ Invalid input. Please enter whole numbers.")

# 🔽 This part makes the program run when you call `python3 ui.py`
if __name__ == "__main__":
    run_simulation()
