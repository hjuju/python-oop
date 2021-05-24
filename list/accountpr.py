class Account:
    def __init__(self, account_number, name, balance):
        self.BANK_NAME = 'SC 은행'
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def get_info(self):
        return f'은행명: {self.BANK_NAME}, 계좌번호: {self.account_number}, 이름: {self.name}'

    @staticmethod
    def create_account_number():
        ls = []



    @staticmethod
    def main():
        while 1:
            menu = input('0. 프로그램 종료:\n1. 계좌 생성\n2. 계좌 출력\n3. 계좌 입금\n4. 계좌 출금\n5. 계좌 삭제\n숫자입력: ')
            if menu == '0':
                print('프로그램을 종료합니다.')
                break
            elif menu == '1':
                pass
            elif menu == '2':
                pass
            elif menu == '3':
                pass
            elif menu == '4':
                pass
            elif menu == '5':
                pass
            else:
                print('잘못 입력했습니다.')
                continue

Account.main()

