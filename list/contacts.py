'''
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''

class Contacs(object):

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_info(self):
        return f'이름: {self.name}, 전화번호: {self.phone}, 이메일: {self.email}, 주소: {self.address}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = int(input('1. 주소록 추가\n0. 프로그램 종료\n2. 출력\n3.삭제\n4.수정\n숫자입력:'))
            if menu == 0:
                print('프로그램을 종료합니다.')
                break
            elif menu == 1:
                ls.append(Contacs(input('이름 입력'), input('전화번호 입력'), input('이메일 입력'), input('주소 입력')))
            elif menu == 2:
                for i in ls:
                   print(f'출력결과: {i.get_info()}')
            elif menu == 3:
                del_name = input('삭제할 이름: ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            elif menu == 4:
                pass
            else:
                print('잘못된 주문입니다.')
                continue

Contacs.main()