import random

class Account(object):

    def __init__(self, account_number, name, money):
        self.BanK_NAME = 'SC은행'
        self.account_number = account_number
        self.name = name
        self.money = money

    def to_string(self):
        return f'은행명: {self.BanK_NAME}, ' \
               f'이름: {self.name}, ' \
               f'계좌번호: {self.account_number}, ' \
               f'잔액: {self.money}, '

    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성
    '''

    @staticmethod
    def create_account_number():
        ls = [str(random.randint(0, 9)) for i in range(3)]
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0, 9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return "".join(ls)

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0. 프로그램 종료\n1. 계좌개설\n2. 계좌목록\n3. 입금\n4. 출금\n5. 계좌탈퇴\n숫자입력: ')
            if menu == '0':
                print('프로그램 종료 합니다.')
                break
            elif menu == '1':
                ls.append(Account(Account.create_account_number(),
                                  input('예금주 입력: '), input('잔액 입력: ')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                account_number = input('입금할 계좌번호 입력: ')
                money = input('입금할 금액 입력: ')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        replace = Account(j.account_number,
                                          j.name,
                                          int(j.money)+int(money))
                        Account.del_account(ls, account_number)
                        ls.append(replace)
            elif menu == '4':
                account_number = input('출금할 계좌번호 입력: ')
                money = input('출금할 금액 입력: ')
                if j.account_number == account_number:
                    replace = Account(j.account_number,
                                      j.name,
                                      int(j.money)-int(money))
                    Account.del_account(ls, account_number)
                    ls.append(replace)
            elif menu == '5':
                Account.del_account(ls, input('제거할 계좌번호 입력:'))
            else:
                print('잘못된 입력 입니다.')
                continue


Account.main()
