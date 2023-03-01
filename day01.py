# --- Day 1: The Tyranny of the Rocket Equation ---

# Parse input
with open('day01.txt') as f:
    mass_list = [int(x) for x in f.readlines()]


# Part one
fuels = [(x // 3 - 2) for x in mass_list]
fuel_needed = sum(fuels)
print(f"Part one answer: Fuel needed --> {fuel_needed}")

# Part two
total = fuel_needed
for fuel in fuels:
    while fuel >= 0:
        fuel = fuel // 3 - 2
        if fuel > 0:
            total += fuel

print(f"Part two answer: Fuel needed --> {total}")
