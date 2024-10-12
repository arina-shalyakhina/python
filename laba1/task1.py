numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
s=0
for e in numbers:
    if e!=None:
        s+=e
s=s/len(numbers)
for i in range(len(numbers)):
    if numbers[i]==None:
        numbers[i]=s
print("Измененный список:", numbers)
