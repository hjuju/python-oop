class Bmi(object):

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def bmidata(self):
        return (self.weight / (self.height / 100) ** 2)

    '''
        고도 비만 : 35 이상
        중(重)도 비만 (2단계 비만) : 30 - 34.9
        경도 비만 (1단계 비만) : 25 - 29.9
        과체중 : 23 - 24.9
        정상 : 18.5 - 22.9
        저체중 : 18.5 미만
    '''

    def get_bmi(self):
        bmi_grade = ''
        bmi_score = int(self.bmidata())

        if bmi_score >= 35:
            bmi_grade = '고도 비만'
        elif bmi_score >= 30:
            bmi_grade = '중(重)도 비만 (2단계 비만)'
        elif bmi_score >= 35:
            bmi_grade = '경도 비만 (1단계 비만)'
        elif bmi_score >= 23:
            bmi_grade = '과체중'
        elif bmi_score >= 18.5:
            bmi_grade = '정상'
        else:
            bmi_grade = '저체중'



        return bmi_grade


    @staticmethod
    def main():
        b = Bmi(int(input('키 입력(cm)')), int(input('몸무게(kg)입력')))
        print(f'BMI 지수는 {int(b.bmidata())} {b.get_bmi()} 입니다.')


Bmi.main()
