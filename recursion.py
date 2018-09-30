# recursion

# find factorial of n! using iteration and recursion and tail recursion
# factorial through iteration
def iter_factorial(x):
    product = 1
    i = 1
    while (i <= x):
        product = product*i 
        i = i+1
    return product

def recursion_factorial(x):
    if ((x == 1) or (x == 0)):
        return 1
    else:
        return x * recursion_factorial(x-1)

# fix this
def tail_factorial(x, result):
    if ((x == 1) or (x == 2)):
        return result
    else:
        return tail_factorial(x-1, result+x)

#print(iter_factorial(5))
#print(recursion_factorial(5))
#print(tail_factorial(5, 0))


# returns sum of the first n integers
def iter_sum(n):
    i = 0
    sum = 0

    while (i <= n):
        sum = sum + i
        i = i + 1
    return sum

# recursion sum of n intevers
def recursive_sum(n):
    if (n == 1) or (n == 0):
        return 1
    else:
        return n + recursive_sum(n-1)

print(iter_sum(5))
print(recursive_sum(5))


# pritn hello world x amount of times
def hello(x):
    if x < 0:
        return 0
    else:
        for i in range(x):
            print ("hello world")

def rec_hello(x):
    if (x == 0):
        print("hello world")
    else:
        print ("hello world")
        return rec_hello(x-1)

rec_hello(5)