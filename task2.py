n = int(input("Input n: "))

#если ряд начинается с 1
def fibonachi1(n):
    if n < 3:
        return 1
    return fibonachi1(n - 1) + fibonachi1(n - 2)

res1 = fibonachi1(n)
print(res1)

#если ряд начинается с 0
def fibonachi0(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return fibonachi0(n - 1) + fibonachi0(n - 2)

res0 = fibonachi0(n)
print(res0)