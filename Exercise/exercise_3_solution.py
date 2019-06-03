# List comprehension
# the first "x" if just a variable
# second "x" is also variable.. name it as you like. just take note that both x should be identical
# the "a" variable is the list above.
# after the a variable is the if condition and the results assign to a num list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = [x for x in a if x < 10]
print(num)

#user input

inp = int(input("Choose a number: "))
num = [x for x in a if x < inp]
print(num)
