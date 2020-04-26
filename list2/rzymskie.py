#!/usr/bin/python

# Oleksandr Khoroshevskyi
# Bioinformatics 1
# UPWr

ROME_SIMBOLS = {
"I": 1,
"V": 5,
"X": 10,
"L": 50,
"C": 100,
"D": 500,
"M": 1000
}
class RomanNumerals():
    """Converting roman numbers to arabic numbers"""

    def __init__(self, rome_string):
        arabic_number = self.calculate_sum(rome_string)
        print("Our number is: ", arabic_number)

    def calculate_sum(self, rome_string):
        arabic_list_length = len(rome_string)
        ar_str = 0
        list_nr = 0

        while list_nr < arabic_list_length:
            value = ROME_SIMBOLS[rome_string[list_nr]]

            if list_nr+1 != len(rome_string):
                if ROME_SIMBOLS[rome_string[list_nr]] < ROME_SIMBOLS[rome_string[(list_nr + 1)]]:
                    value = - ROME_SIMBOLS[rome_string[list_nr]]

            ar_str += value
            list_nr += 1
        return(ar_str)

if __name__ == "__main__":
    RomanNumerals("CMIV")
    
