words = ["abc", "aba", "xy", "1221", "aa"]
count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1 

print(count)
