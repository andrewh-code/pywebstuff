import functools


# anonymous functions/lambda function
anonymous = lambda x: x+1
print(anonymous(5))
# take sum functional programming
sum = lambda x,y: x+y 
print (sum(1,2))

# filter, reduce, map, max, min, etc

# pass in an anonymous function to a higher order
my_list = [1,2,3,4,5,6,7,8,9,10]
unordered_list = [10,7,3,5,6,1,2,4,8,9]

# use map to multiply each element in the list by 2 (use anonymous function)
new_list = list(map(lambda x: x*2, my_list))
print(new_list)

# use filter to find elements that are only divisible by 2 (use anonymous function as well)
new_list = list(filter(lambda x: x%2==0, my_list))
print(new_list)

# use filter to find elements that are greater than 5
new_list = list(filter(lambda x: x > 5, my_list))
print (new_list)

# display powers of two (my_list are the powers 2**x)
new_list = list(map(lambda x: 2**x, my_list))
print (new_list)

# reduce all the numbers in the list and sum them into one value
sum = functools.reduce(lambda x,y: x+y, my_list)
print (sum)

# find the max value in the list
anonymous = lambda x,y: x if (x > y) else y 
max_value = functools.reduce(anonymous, my_list)
print (max_value)

# find the minimum value in the list
min_value = functools.reduce(lambda x,y: x if (x < y) else y, my_list)
print(min_value)


new_list = sorted(unordered_list)
print (new_list)


# find length of a list
length = functools.reduce(lambda x,y: , unordered_list)
print (length)