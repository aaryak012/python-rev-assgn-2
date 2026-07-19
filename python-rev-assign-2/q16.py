#Q16
def double_and_filter(numbers):
    result = []
    
    for num in numbers:
        doubled = num * 2
        if doubled > 10:
            result.append(doubled)
    
    return result
print(double_and_filter([3, 8, 6]))   
print(double_and_filter([7, 8, 9]))   