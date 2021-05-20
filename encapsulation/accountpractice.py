import random as rd

class Accountp(object):

    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.balance = "0"
        self.num1 = rd.randint(0, 999)
        self.num2 = rd.randint(0, 99)
        self.num3 = rd.randint(0, 999999)

    def get_info(self):
        return f'예금주: {self.name}, 은행명: {self.bank}, 잔액: {self.balance}, 계좌번호: {str(self.num1).zfill(3)}-{str(self.num2).zfill(2)}-{str(self.num3).zfill(6)}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = (input('0. 프로그램 종료\n1. 계좌 생성\n2. 생성계좌 출력\n3. 계좌 삭제\n4. 계좌 수정\n번호 입력: '))
            if menu == 0:
                print('프로그램이 종료되었습니다.')
                break
            elif menu == '1':
                ls.append(Accountp(input('예금주: '), input('은행명: ')))
            elif menu == '2':
                for i in ls:
                    print(f'결과출력: {i.get_info()}')
            elif menu == '3':
                del_name = input('삭제할 계좌 예금주 입력: ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
                        print('삭제 성공!')
            elif menu == '4':
                edit_name = input('수정할 계좌 예금주 입력: ')
                edit_info = Accountp(edit_name,input('수정할 은행명 입력: '))
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)
                print('수정 완료!')
            else:
                print('잘못 선택했습니다.')
                continue

Accountp.main()