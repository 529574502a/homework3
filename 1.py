def sqrt(number):
    if number < 0 or number > 100:
        return False
    return round(number ** 0.5,2)
number = int(input('输入一个100以内的整数'))
result = sqrt(number)
print(f"结果为{result}")