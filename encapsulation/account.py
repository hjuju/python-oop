import random

class Account(object):
    def __init__(self, depositer, balance):
        self.depositer = depositer
        self.balance = balance
        self.bank = 'SC은행'
        self.firstacc = random.randint(0, 999)
        self.secondacc = random.randint(0, 99)
        self.thirdacc = random.randint(0, 999999)

    def get_info(self):
        return f'예금주: {self.depositer}, 잔액: {self.balance}, 은행명: {self.bank}, 계좌번호: {self.firstacc}-{self.secondacc}-{self.thirdacc}'


    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0. 프로그램종료\n1. 계좌 생성\n2. 출력\n3. 삭제\n4. 수정\n숫자 입력: ')
            if menu == '0':
                print('프로그램을 종료합니다.')
                break
            elif menu == '1':
                ls.append(Account(input('예금주: '), input('잔액: ')))
            elif menu == '2':
                for i in ls:
                    print(f'출력결과: {i.get_info()}')
            elif menu == '3':
                del_name = input('삭제할 예금주: ')
                for i, j in enumerate(ls):
                    if j.depositer == del_name:
                        del ls[i]
            elif menu == '4':
                edit_name = input('수정할 예금주: ')
                edit_info = Account(edit_name, input('잔액 수정: '))
                for i, j in enumerate(ls):
                    if j.depositer == edit_name:
                        del ls[i]
                        ls.append(edit_info)
            else:
                print('잘못 입력했습니다.')
                continue

Account.main()
