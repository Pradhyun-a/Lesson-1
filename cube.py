def cube(num):
    return num * num * num

def check(num):
    if num % 3 == 0:
        result = cube(num)
        print(result)
    else:
        print("This number is not divisible by 3")
check(6) 
