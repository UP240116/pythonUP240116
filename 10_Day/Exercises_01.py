#LEVEL 1
#1.Iterate 0 to 10 using for loop, do the same using while loop.
print("Using a for loop:")
for i in range(11):  
    print(i)

print("\nUsing a while loop:")
i = 0
while i <= 10:
    print(i)
    i += 1

#2.Iterate 10 to 0 using for loop, do the same using while loop.
print("Using a for loop:")
for i in range(10, -1, -1):  
    print(i)

print("\nUsing a while loop:")
i = 10
while i >= 0:
    print(i)
    i -= 1

#3.Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):
    print('#' * i)

#4.Use nested loops to create the following:
for i in range(8):
    for j in range(8):
        print("# ", end="")  
    print()  

#5.Print the following pattern:
for i in range(11):  
    result = i * i
    print(f"{i} x {i} = {result}")

#6.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
technologies = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in technologies:
    print(item)

#7.Use for loop to iterate from 0 to 100 and print only even numbers
for num in range(0, 101, 2): 
    print(num)

#8.Use for loop to iterate from 0 to 100 and print only odd numbers
for num in range(0, 101):
    if num % 2 != 0:  
        print(num)

for num in range(1, 101, 2): 
    print(num)

