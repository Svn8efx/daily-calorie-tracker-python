# Name: Anish
# Date: 05/10/25
# Project: Daily Calorie Tracker
# Description   : Track your meals, calories, and check if you meet your daily goal.

print("Welcome to your Personal Calorie Monitor!")
print("Let's check how healthy your day has been.\n")

food_items = []      # stores food names
energy_values = []   # stores calorie values

#Meal Counter
meal_count = int(input("🍽️ How many meals or snacks did you have today? "))

#Loop to get meal data
for i in range(meal_count):
    name = input(f"\nEnter the name of food item {i+1}: ") #food name
    cal = float(input(f"Enter calories for {name}: ")) #calories count

#Appending the meal data to the list
    food_items.append(name)
    energy_values.append(cal)

print("\nAwesome! Data recorded successfully ")

#calculating the total calories
sum_energy = sum(energy_values)

#calculating the average calories
avg_energy = sum_energy / len(energy_values)

#asking for the daily limt
target_limit = float(input("\nNow tell me, what's your calorie goal for today? "))

print("\n Checking your results...\n")
print("Food Item\t\tEnergy (kcal)")

# 40 dashes for a line
print("-" * 40)

# Loop to print each meal with its calories
for i in range(len(food_items)):
    print(f"{food_items[i]}\t\t{energy_values[i]}")

# 40 dashes for a line
print("-" * 40)

# Print total and average
print(f"Total:\t\t\t{sum_energy}")
print(f"Average:\t\t{avg_energy:.2f}") # .2f means 2 decimal place

#exceed limit warning
if sum_energy > target_limit:
    print("\n Oops! You've gone beyond your daily limit.")
    print("Try reducing a bit next time for a balanced day!")
else:
    print("\n Great! You stayed within your goal today. Keep it up!")

