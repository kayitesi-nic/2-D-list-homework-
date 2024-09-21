A= [] #val>15

for i in range(20):
    val= int(input("How many values do you want?:"))

    if val>15:
        A.sort()
        A.reverse()
        A.append(val)
    
print(A)
