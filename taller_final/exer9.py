def factorial(num):
    result= 0
    for value in range(1, num+1):
        result*= value

    return result

print(factorial(5))

def fibonacci(termino):
    result= 1
    for num1 in range(termino):
        num1= num1+result
        result= num1+result

    return result

print(fibonacci(6))

def sum_dig(num):
    result=int()
    str_nums= list(str(num))
    for nums in str_nums:
        result+= int(nums)

    return result

print(sum_dig(1596))