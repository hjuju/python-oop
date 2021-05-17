class Bmi:
    def bmidata(self, weight, height):
        self.weight = weight
        self.height = height

    def bmi_level(self):
        result = (b.weight / (b.height/100)**2)
        return round(result,1)

if __name__ == '__main__':
    b = Bmi()
    b.bmidata(60, 180)
    round_bmi = b.bmi_level()

if round_bmi <= 18.5:
    print("BMI 지수:", round_bmi, "저체중 입니다.")
elif round_bmi <= 23:
    print("BMI 지수", round_bmi, "정상체중 입니다.")
elif round_bmi <= 25:
    print("BMI 지수", round_bmi, "과체중 입니다.")
elif round_bmi <= 30:
    print("BMI 지수", round_bmi, "비만 입니다.")
else:
    print("BMI 지수", round_bmi, "고도비만 입니다.")


