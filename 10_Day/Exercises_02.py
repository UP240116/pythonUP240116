#LEVEL 2
#1.1.Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total_sum = 0

for num in range(0, 101):
    total_sum += num

print(f"The sum of all numbers is {total_sum}.")

#1.2.Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens = 0
sum_odds = 0

for num in range(0, 101):
    if num % 2 == 0:  
        sum_evens += num
    else:  
        sum_odds += num

print(f"The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.")
