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
        rome_list = self.create_rome_list(rome_string)
        arabic_list = self.rome_list_to_arabic(rome_list)
        arabic_number = self.calculate_sum(arabic_list)
        print("Our number is: ", arabic_number)

    def create_rome_list(self, rome_string):
        rome_list = list(rome_string)
        return(rome_list)

    def rome_list_to_arabic(self,rome_list):
        arabic_list = []
        for symbol in rome_list:
            arabic_list.append(ROME_SIMBOLS[symbol])
        return(arabic_list)

    def calculate_sum(self, arabic_list):
        self.arabic_list = arabic_list
        arabic_list_length = len(self.arabic_list)
        ar_str = 0
        self.list_nr = 0

        while self.list_nr < arabic_list_length:
            value = self.arabic_list[self.list_nr]

            if self.list_nr == len(self.arabic_list):
                if self.arabic_list[self.list_nr] < self.arabic_list[(self.list_nr + 1)]:
                    value = - self.arabic_list[self.list_nr]

            ar_str += value
            self.list_nr += 1
        return(ar_str)

if __name__ == "__main__":
    RomanNumerals("MMDCCLXXXIV")
