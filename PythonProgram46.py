# Map and Filter Function

def square(x):
    return x*x


num = [1, 2, 3, 4, 5]
result = list(map(square, num))
print(result)

#Filtering Function
num = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, num))
print(result)
