from functools import reduce

expense = [("dinner", 80),("gas", 120)]
           
my_reducer = lambda a, b: a[1] + b[1]

sum = reduce(my_reducer, expense)

print(sum)