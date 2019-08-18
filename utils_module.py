#Utils module

def find_max(numbers):
    maxnum = numbers[0]
    for number in numbers:
        if maxnum < number:
            maxnum = number
    return maxnum
