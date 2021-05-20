class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


    @staticmethod
    def main():
        while 1:
            menu = int((input('0.프로그램 종료\n1.종목추가\n숫자입력:')))
            if menu == 0:
                print('프로그램을 종료합니다.')
                break

            elif menu == 1:
                s = Stock(input('종목명'), input('종목 코드'))
                print(f'종목명: {s.get_name()}, 종목 코드: {s.get_code()}')

            else:
                print('잘못 입력하셨습니다.')
                continue

Stock.main()


