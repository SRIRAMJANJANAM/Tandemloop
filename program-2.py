a = int(input("Enter a number (a): "))
if a % 2 == 0:
    a -= 1

odd_numbers = []
num = 1
for _ in range(a):
    odd_numbers.append(num)
    num += 2

print("input =",a,", then Output:", ', '.join(map(str, odd_numbers)))
