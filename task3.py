a = int(input("Input a = "))
b = int(input("Input b = "))
c = int(input("Input c = "))

res = max(a, b, c) + max(min(a, b), min(b, c), min(a, c))

print(f"Sum of 2 biggest: {res}")    