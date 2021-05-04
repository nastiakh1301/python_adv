fin_result = 0
temp = True
while temp == True:
    n = input("Input numbers or @ to complete the program: ").split()
    interm_result = 0
    for i in range(len(n)):
        if n[i] == '@':
            temp = False
            break
        else:
            interm_result = interm_result + int(n[i])
    fin_result = fin_result + interm_result
    print(f"Intermediate result: {fin_result}")
print(f"Final result: {fin_result}")


