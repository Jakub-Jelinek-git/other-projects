def romanToInt(s):
        romans = {"I": 1, "V": 5, "X": 10, "L":50,  "C": 100, "D": 500, "M": 1000}

        value = 0
        last_value = 0
        for rom_didget in s[::-1]:
            dig_value = romans[rom_didget]
            if dig_value >= last_value:
                value += dig_value
                last_value = dig_value
            else:
                value -= dig_value
            print(value, end = ": ")
            print(dig_value, end = ", ")
            print(last_value)
        return value

print(romanToInt("MCMXCIV"))