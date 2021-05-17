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