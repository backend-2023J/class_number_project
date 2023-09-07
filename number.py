import math

class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value%2==1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value%2==0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        count = 0
        if self.value == 1:
            return 'Oh no 1'
        elif self.value>1:
            for i in range(1,self.value+1):
                if self.value%i==0:
                    count += 1
            return count<=2
        else:
            return f'{self.value} is negative number'

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        lst_divisors = []
        for i in range(1,self.value+1):
            if self.value%i==0:
                lst_divisors.append(i)
        return lst_divisors

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        return [i for i in str(self.value)]

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.value)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return self.value == int(str(self.value)[::-1])

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return [int(i) for i in str(self.value)]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max([int(i) for i in str(self.value)])

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min([int(i) for i in str(self.value)])

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return sum([int(i) for i in str(self.value)])/len(str(self.value))

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        if len(str(self.value))%2==1:
            position = math.ceil(len(str(self.value))/2-1)
            return float(str(self.value)[position])
        else:
            position = math.ceil(len(str(self.value))/2)
            return float(str(self.value)[position-1]), float(str(self.value)[position])

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return [i for i in range(1, self.value+1)]

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(4214)
print("Number is:", number.get_number())
print(f'{number.value} is odd:', number.is_odd())
print(f'{number.value} is even:', number.is_even())
print(f'{number.value} is prime:', number.is_prime())
print(f'{number.value}\'s divisors:', number.get_divisors())
print(f'{number.value} was reverse:', number.get_reverse())
print(f'{number.value} is palindrome:', number.is_palindrome())
print(f'{number.value}\'s digits:', number.get_digits())
print("Max digit:", number.get_max())
print("Min digit:", number.get_min())
print(f'{number.value} - average of digits:', number.get_average())
print("Median:", number.get_median())
print('Range:', number.get_range())