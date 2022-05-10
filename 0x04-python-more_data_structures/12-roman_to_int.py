#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string and type(roman_string) == str):
        length = len(roman_string)
        result = 0
        i = 0
        while i < length:
            if roman_string[i] == "M":
                if roman_string[i - 1] == "C":
                    result += 800
                else:
                    result += 1000
            elif roman_string[i] == "D":
                result += 500
            elif roman_string[i] == "C":
                if roman_string[i - 1] == "X":
                    result += 80
                else:
                    result += 100
            elif roman_string[i] == "L":
                result += 50
            elif roman_string[i] == "X":
                if roman_string[i - 1] == "I":
                    result += 8
                else:
                    result += 10
            elif roman_string[i] == "V":
                result += 5
            elif roman_string[i] == "I":
                result += 1
            i += 1
        return (result)
    else:
        return (0)
