def add_function(first, second):
    return first + second

def sub_function(first, second):
    return first - second

def mul_function(first, second):
    return first * second

def div_function(first, second):
    return first / second


class Bmi:
    def bmidata(self,weigt, height):
        self.weight = weigt
        self.height = height

    def bmi(self):
        result = (self.weight / self.height**2)
        return round(result,1)

if __name__ == '__main__':
    b = Bmi()
    b.bmidata(60,1.7)
    roundbmi = b.bmi()

print(roundbmi)

print(add_function(0, 1))
print(sub_function(3, 2))
print(mul_function(1, 1))
print(div_function(1, 1))