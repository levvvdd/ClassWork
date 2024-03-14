matrix = [[1,2,3], [4,5,6], [7,8,9]]

print("matrix")
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
    
print ("нечетные числа matrix:")
for row in matrix:
    for num in row:
        if num % 2 != 0:
            print(num, end=" ")
print()

even_count = sum(1 for orw in matrix for num in row if num % 2 == 0)
print ("количество чётных чисел:", even_count)