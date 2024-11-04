a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
odds = []
for num in a:
    if num % 2 != 0:
        odds.append(num)
print(odds)
