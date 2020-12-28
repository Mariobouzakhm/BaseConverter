# Helps convert between the numerical and alphabetical representation of the numbers between 11 and 15 (inclusive).
conversion_table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def convertToBaseN(n, number):
    """
    (int, int) -> str

    Given a base n and a number in base-10, convert the number to its form in base n.

    >>> convertToBaseN(2, 100)
    '1100100'
    >>> convertToBaseN(16, 64)
    '40'
    >>> convertToBaseN(12, 142)
    'BA'
    """

    # String that represent the converted number.
    converted = ""

    # Algorithm that converts the number from base-10 to base-n.
    # It works by successfully dividing the number by n, and then adding the remainder of this division in the begining of converted.
    while number != 0:
        remainder = number % n
        number //= n
        
        # Make sure to catch the cases where the remainder is bigger than 10 (for base > 10)
        if remainder > 9:
            converted  = conversion_table[remainder] + converted
        else:
            converted = str(remainder) + converted

    return converted

def convertFromBaseN(n, number):
    """
    (int, str) -> int

    Given a base n and a number in base-n, convert the number to its form in base 10.

    >>> convertFromBaseN(2, '10010011')
    147
    >>> convertFromBaseN(7, '63545') 
    15713
    >>> convertFromBaseN(13, 'BBA9B')
    340156
    """
    
    # Reverse the input number for easier conversion.
    number = str(number[::-1])
    # Contains the number converted to base 10.
    converted = 0
    
    # Algorithm to convertr from base n to base 10.
    # It work by adding powers of n times the digit that represents it.
    for i in range(len(number)):
        value = number[i]
        if value in conversion_table:
            converted += conversion_table[value] * n ** i
        else:
            converted += int(value) * n ** i
            
    return converted

def convertFromNtoN(beginN, endN, number):
    """
    (int, int, str)

    Given two integers beginN and endN, converts the number which is in base beginN to base endN.

    >>> convertFromNtoN(2, 4, '10010011101')
    '102131'
    >>> convertFromNtoN(10, 11, '11')
    '10'
    >>> convertFromNtoN(16, 2, 'FFEFF23')
    '1111111111101111111100100011'
    """

    # Shortcuts to avoid performing multiple calculation, if beginN or endN is 10.
    if endN == 10:
        return convertFromBaseN(beginN, number)
    
    if beginN == 10:
        return convertToBaseN(endN, int(number))

    # Performs a conversion from beginN to endN.
    return convertToBaseN(endN, convertFromBaseN(beginN, number))

if __name__ == "__main__":
    import doctest
    doctest.testmod()