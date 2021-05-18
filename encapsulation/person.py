'''
이름, 출생년도, 주소를 입력 받아서
회원가입한 사람의 이름, 나이(만), 주소를 출력하시오
'''

class Person:
    def __init__(self, name, birthyear, adress):
        self.name = name
        self.birthyear = birthyear
        self.adress = adress

    def membername(self):
        return self.name

    def memberage(self):
        year = int(self.birthyear)
        return 2020 - year

    def memberadress(self):
        return self.adress


    @staticmethod
    def main():
        p = Person(input('이름 입력'), int(input('출생년도 입력(ex1997)')),input('주소입력'))
        print(f'이름: {p.membername()}')
        print(f'나이: {p.memberage()}')
        print(f'주소: {p.memberadress()}')

Person.main()

