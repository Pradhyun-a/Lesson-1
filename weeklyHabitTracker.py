habit_info = ("Reading", True, 30, 25.5)
print(habit_info)

weekly_habits = (1, 0, 1, 1, 0, 1, 0)
print(weekly_habits)

print(len(weekly_habits))

print(weekly_habits[0])
print(weekly_habits[3])
print(weekly_habits[0:3])
print(weekly_habits[5:7])

new_habits = weekly_habits + (1,)
print(new_habits)

completed = weekly_habits.count(1)
missed = weekly_habits.count(0)

print("Completed days:", completed)
print("Missed days:", missed)
print("Good job keeping up with your habit!")
