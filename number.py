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

        s=0
        for i in range(1,self.value+1):
            if (self.value%i==0):
                s+=1
        if s==2:
            return True
        else:
            return False


    def get_divisors(self):
        """
            Returns a list of all the divisors of the number.

            returns: list
        """

        a=[]
        for i in range(1,self.value+1):
            if self.value%i==0:
                a.append(i)
        return a
        


    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """

        a=len(str(self.value))
        return int(a)


    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """

        i = 0
        while self.value>0:
            i+=self.value%10
            self.value //= 10
        return i
=======
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

        if  (self.value[::-1]==self.value):
            return True
        
        return False


    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """

        a=[]
        for i in str(self.value):
            if i.isdigit()==1:
               a.append(i)    
        return a
    


    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """

        a=[]
        for i in  str(self.value):
            if i.isdigit()==1:
                a.append(int(i))
        return max(a)


    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """

        b = []
        for i in str(self.value):
            if i.isdigit()==1:
                b.append(int(i))
        return min(b)


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
    


number = Number("18")
print(number.get_reverse())

