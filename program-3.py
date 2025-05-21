numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

multiples_count = {i: 0 for i in range(1, 10)}


for num in numbers:
    for i in range(1, 10):
        if num % i == 0:
            multiples_count[i] += 1

print(multiples_count)
