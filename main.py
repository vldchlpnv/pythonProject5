from functools import total_ordering
@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number
        self.number_rim = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        self.res = 0

    @staticmethod
    def int_to_roman(number):
        int_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
                     10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                     100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        result = ''
        for n in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
            while n <= number:
                result += int_roman[n]
                number -= n
        return result

    def __str__(self):
        return f'{self.number}'


    def __int__(self):
        
        for i in range(len(self.number) - 1):
            if (self.number_rim[self.number[i]] < self.number_rim[self.number[i + 1]]):
                self.res = self.res - self.number_rim[self.number[i]]
            elif (self.number_rim[self.number[i]] >= self.number_rim[self.number[i + 1]]):# перевод из римских в арабские не мой алгоритм мой не работал надо переделать
                self.res = self.res + self.number_rim[self.number[i]]

        self.res = self.res + self.number_rim[self.number[len(self.number) - 1]]

        return self.res

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number == other.number
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number > other.number
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            a1 = int(self)  #инетерное действие сам бы не догадался
            a2 = int(other) #инетерное действие сам бы не догадался
            return RomanNumeral(RomanNumeral.int_to_roman(a1+a2)) #инетерное действие сам бы не догадался
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            a1 = int(self) #тут видимо мы переводим строкое значение римской цифры в значение арабское посредством магического метода инт который задали выше
            a2 = int(other)
            return RomanNumeral(RomanNumeral.int_to_roman(a1 - a2)) # здесь применяем метод перевода из арабскимх в римские после того как он все посчитает а вызываем его через класс
        #соответсвтенно отсюда и появляется второй RomanNumeral ну и аргументы соответсвтенно в которых ведется подсчет

        return NotImplemented
