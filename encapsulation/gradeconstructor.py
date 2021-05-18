class Grade:

    def __init__(self, kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def sum(self):
        return self.kor + self.eng + self.mat

    def avg(self):
        return self.sum() / 3

    @staticmethod
    def main():
        g = Grade(int(input('국어점수 입력')), int(input('영어점수 입력')), int(input('수학점수 입력')))
        print(f'{g.kor} + {g.eng} + {g.mat} = {g.sum()}')
        print(f'{g.sum()} / 3 = {g.avg()}')

Grade.main()
