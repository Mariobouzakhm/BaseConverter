conversion_table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def convertToBaseN(n, number):
    converted = ""

    while number != 0:
        remainder = number % n
        number //= n
        
        if remainder > 9:
            converted  = conversion_table[remainder] + converted
        else:
            converted = str(remainder) + converted

    return converted

def convertFromBaseN(n, number):
    number = str(number[::-1])
    converted = 0
    
    for i in range(len(number)):
        value = number[i]
        if value in conversion_table:
            converted += conversion_table[value] * n ** i
        else:
            converted += int(value) * n ** i
            
    return converted

def convertFromNtoN(begin, end, number):
    return convertToBaseN(end, convertFromBaseN(begin, number))


if __name__ == "__main__":
    n = 12
    number = 'BA'

    toN = 11


    print(convertFromNtoN(n, toN, number))